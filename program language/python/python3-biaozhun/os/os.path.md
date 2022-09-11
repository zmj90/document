```python
import os.path as path


p = path.abspath("py.py")
p1 = path.abspath(__file__)
print(p)
# D:\doing\study\demo\python_project\demo\py.py
print(p1)
# D:\doing\study\demo\python_project\demo\demo_os_path.py
p2 = path.basename(__file__)
print(p2)
# demo_os_path.py
p3 = path.dirname(__file__)
print(p3)
# D:\doing\study\demo\python_project\demo
p4 = path.join(p3, p2)
print(p4)
# D:\doing\study\demo\python_project\demo\demo_os_path.py
p5 = path.split(p4)
print(p5)
# ('D:\\doing\\study\\demo\\python_project\\demo', 'demo_os_path.py')

f1 = path.getsize(__file__)
# 功能： 获取文件大小, 参数： 指定文件, 返回值： 文件大小
print(f1, type(f1))

# path.exists(file)
# 功能： 查看文件是否存在, 参数： 指定文件, 返回值：存在返回True，不存在返回False

# path.isfile(file)
# 功能： 判断文件类型, 参数： 指定文件, 返回值：普通文件返回True，否则返回False


```



```python
import os


path = os.getcwd()
print(path, type(path))
# D:\doing\study\demo\python_project\demo <class 'str'>
# os.system("dir")
print(__file__, type(__file__))
# D:\doing\study\demo\python_project\demo\demo_os.py <class 'str'>
print(dir())
# for i in dir():
#     print(eval(i))
# print(eval('__import__("os").system("dir")'))

l1 = os.listdir(os.getcwd())
l2 = os.listdir(".")
# 功能： 查看文件列表, 参数： 指定目录, 返回值：目录中的文件名列表
print(l1, type(l1))
print(l2, type(l2))

# os.remove(file)
# 功能： 删除文件, 参数： 指定文件
```
