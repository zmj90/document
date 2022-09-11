```python
# 时间戳
time.time()
time.mktime(t)


# 结构化时间对象
time.gmtime([secs])
time.localtime([secs])
time.strptime(string[, format])


# （格式化）时间字符串
time.ctime([secs])
time.strftime(format[, t])
time.asctime([t])


# 时间戳-结构化时间对象
# UTC
time.gmtime([secs])
# local
time.localtime([secs])


# 结构化时间对象-时间戳
time.mktime(t)


# 结构化时间对象-时间字符串
time.asctime([t])
time.strftime(format[, t])


# 时间字符串-结构化时间对象
time.strptime(string[, format])


# 时间戳-时间字符串
time.ctime([secs])


# sleep
time.sleep(secs)
```

