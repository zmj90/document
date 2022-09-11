# datetime

```python
import time
from datetime import timedelta, date, time as t, datetime

# ----------------------------timedelta
y = timedelta(days=3)
print(f"{y=}, {type(y)=}")
# y=datetime.timedelta(days=3), type(y)=<class 'datetime.timedelta'>
print(y)
# 3 days, 0:00:00

# ------------------------------date
# 日期对象
d1 = date.fromtimestamp(time.time())
print(f"{d1=}, {type(d1)=}")
# d1=datetime.date(2022, 3, 12), type(d1)=<class 'datetime.date'>
d = y + d1
print(f"{d=}, {type(d)=}")
d2 = date.today()
print(f"{d2=}, {type(d2)=}")
# print(f"{d2.year=}, {type(d2.year)=}"
#       f"{d2.month=}, {type(d2.month)=}"
#       f"{d2.day=}, {type(d2.day)=}")
# d1=datetime.date(2022, 3, 12), type(d1)=<class 'datetime.date'>
d3 = date.fromisoformat("2022-04-12")
print(f"{d3=}, {type(d3)=}")
# d3=datetime.date(2022, 4, 12), type(d3)=<class 'datetime.date'>
print(f"{date.min=}, {type(date.min)=}")
d7 = date(2022, 5, 16).timetuple()
print(f"{d7=}, {type(d7)=}")
# d7=time.struct_time(tm_year=2022, tm_mon=5, tm_mday=16, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=136, tm_isdst=-1), type(d7)=<class 'time.struct_time'>
d8 = date(2022, 5, 16).replace(2025)
print(f"{d8=}, {type(d8)=}")
# d8=datetime.date(2025, 5, 16), type(d8)=<class 'datetime.date'>

# 日期字符串
d4 = date(2022, 5, 16).ctime()
print(f"{d4=}, {type(d4)=}")
# d4='Mon May 16 00:00:00 2022', type(d4)=<class 'str'>
d5 = date(2022, 5, 16).strftime("%Y,%m,%d")
print(f"{d5=}, {type(d5)=}")
# d5='2022,05,16', type(d5)=<class 'str'>
d6 = date(2022, 5, 16).isoformat()
print(f"{d6=}, {type(d6)=}")
# d6='2022-05-16', type(d6)=<class 'str'>

# ------------------------------datetime
# 日期时间对象
dt1 = datetime.today()
print(f"{dt1=}, {type(dt1)=}")
# dt1=datetime.datetime(2022, 3, 13, 9, 30, 22, 113951), type(dt1)=<class 'datetime.datetime'>
dt2 = datetime.now()
print(f"{dt2=}, {type(dt2)=}")
# dt2=datetime.datetime(2022, 3, 13, 9, 30, 22, 113951), type(dt1)=<class 'datetime.datetime'>
dt3 = datetime.fromtimestamp(time.time())
print(f"{dt3=}, {type(dt3)=}")
# dt3=datetime.datetime(2022, 3, 13, 9, 34, 37, 333077), type(dt3)=<class 'datetime.datetime'>
dt4 = datetime.utcfromtimestamp(time.time())
print(f"{dt4=}, {type(dt4)=}")
# dt4=datetime.datetime(2022, 3, 13, 1, 35, 36, 318019), type(dt4)=<class 'datetime.datetime'>
dt5 = datetime.strptime("2023/02/10", "%Y/%m/%d")
print(f"{dt5=}, {type(dt5)=}")
# dt5=datetime.datetime(2023, 2, 10, 0, 0), type(dt5)=<class 'datetime.datetime'>

# 日期时间字符串
dt6 = dt1.strftime("%Y/%m/%d %H:%M:%S")
print(f"{dt6=}, {type(dt6)=}")
# dt6='2022/03/13 09:43:31', type(dt6)=<class 'str'>
dt7 = dt1.strftime("%Y/%m/%d")
print(f"{dt7=}, {type(dt7)=}")
# dt7='2022/03/13', type(dt7)=<class 'str'>

```

