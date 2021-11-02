#!/bin/sh

# ホスト側ユーザーのUIDとGIDを.envファイルに事前に書き出しておく
# ここで書き出したUIDとGIDでmysqlコンテナ内でフォルダ捜査権限を与える
echo "LINUX_MYSQL_UID=$(id -u $USER)" >> .env
echo "LINUX_MYSQL_GID=$(id -g $USER)" >> .env