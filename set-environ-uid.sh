#!/bin/sh
echo "LINUX_MYSQL_UID=$(id -u $USER)" >> .env
echo "LINUX_MYSQL_GID=$(id -g $USER)" >> .env