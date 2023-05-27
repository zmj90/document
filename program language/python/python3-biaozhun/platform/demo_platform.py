import platform

v1 = platform.python_version()
print(v1, type(v1))
# 3.9.6 <class 'str'>


v2 = platform.platform()
print(v2, type(v2))
# Windows-10-10.0.19045-SP0 <class 'str'>


v3 = platform.system()
print(v3, type(v3))
# Windows
