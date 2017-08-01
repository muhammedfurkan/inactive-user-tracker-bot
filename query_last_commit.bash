#!/usr/bin/env bash
sqlite3 messages.db -column <<SQL
SELECT * FROM message
WHERE commit_count >= 10
ORDER BY last_commit DESC
LIMIT 50;
SQL