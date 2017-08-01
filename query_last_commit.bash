#!/usr/bin/env bash
sqlite3 messages.db -column <<SQL
SELECT * FROM message
ORDER BY last_commit DESC
LIMIT 30;
SQL
