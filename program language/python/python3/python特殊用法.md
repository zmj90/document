# range

```python
# 表示不可变的数字序列
ls = ["a", "b"]
# for i in range(len(ls)):
for i in ls:
    ls.append(f"a{i}")
    ls.append(f"b{i}")
    if len(ls) > 10:
        break
print(ls)

```

