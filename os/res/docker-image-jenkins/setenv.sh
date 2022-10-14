#!/bin/sh
# 解决jenkins日志乱码
JAVA_OPTS="$JAVA_OPTS -Dfile.encoding=utf-8"