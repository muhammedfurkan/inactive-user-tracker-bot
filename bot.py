#!/usr/bin/env python
import json
import logging

from telegram.ext import Updater, MessageHandler, Filters

from model import Message, db

configure = json.load(open('configure.json'))


def new_message(bot, update):
    chat_id = update.message.chat.id
    from_id = update.message.from_user.id
    message_date = update.message.date

    if chat_id not in configure['allow-groups']:
        status = bot.leave_chat(chat_id)
        logging.info('chat_id: %s not allow groups, leave chat: %s', chat_id, status)
        return

    message, created = Message.get_or_create(
        chat_id=chat_id, from_id=from_id,
        defaults=dict(last_commit=message_date, commit_count=0)
    )
    if not created:
        message.commit_count += 1
    message.save()
    logging.info(
        '%s | %s | %-15s | %-11s',
        'created' if created else 'updated',
        message_date, chat_id, from_id
    )


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        filename=configure.get('logging', None)
    )

    db.connect()
    if not Message.table_exists():
        Message.create_table()

    updater = Updater(configure['token'])
    updater.dispatcher.add_handler(MessageHandler(Filters.all, new_message))
    updater.start_polling()


if __name__ == '__main__':
    main()
