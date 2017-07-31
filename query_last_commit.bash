#!/usr/bin/env bash
echo 'SELECT * FROM message ORDER BY last_commit DESC;' | sqlite3 messages.db -column