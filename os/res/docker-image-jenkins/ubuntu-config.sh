#!/bin/sh
# 更换源
cp /etc/apt/sources.list /etc/apt/sources.list.bak
sed -ri "s/(archive|security).ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata
apt-get -y install apt-utils sudo vim fontconfig inetutils-ping net-tools locales wget git mysql-client \
make gcc zlib* build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev libgdbm-dev libgdbm-compat-dev