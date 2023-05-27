import os.path as path


p = path.abspath("py.py")
print(p, type(p))
# D:\doing\study\demo\python_project\standard\py.py <class 'str'>

p1 = path.abspath(__file__)
print(p1, type(p1))
# D:\doing\study\demo\python_project\standard\demo_os_path.py <class 'str'>

p2 = path.basename(__file__)
print(p2, type(p2))
# demo_os_path.py <class 'str'>

p3 = path.dirname(__file__)
print(p3, type(p3))
# D:\doing\study\demo\python_project\standard <class 'str'>

p4 = path.join(p3, p2)
print(p4, type(p4))
# D:\doing\study\demo\python_project\standard\demo_os_path.py <class 'str'>

p5 = path.split(p4)
print(p5, type(p5))
# ('D:\\doing\\study\\demo\\python_project\\standard', 'demo_os_path.py') <class 'tuple'>

# f1 = path.getsize(__file__)
# 功能： 获取文件大小, 参数： 指定文件, 返回值： 文件大小
# print(f1, type(f1))

# path.exists(file)
# 功能： 查看文件是否存在, 参数： 指定文件, 返回值：存在返回True，不存在返回False

# path.isfile(file)
# 功能： 判断文件类型, 参数： 指定文件, 返回值：普通文件返回True，否则返回False

