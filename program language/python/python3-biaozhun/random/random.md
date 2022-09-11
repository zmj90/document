```python
import random


# -------------------- bytes methods ---------------------
b = random.randbytes(5)
print(b, type(b))
# b'\x82\x05X\xe9`' <class 'bytes'>

# -------------------- integer methods  -------------------
i = random.randrange(3)  # 不含端点
print(f"{i=},  {type(i)=}")
# i=0,  type(i)=<class 'int'>
# random.randrange(start, stop[, step])

i1 = random.randint(-1, 1)  # 含端点
print(f"{i1=}, {type(i1)=}")
# i1=3, type(i1)=<class 'int'>

# -------------------- sequence methods  -------------------
s = random.choice([1, "2", 3, 4, 5])
print(f"{s=}, {type(s)=}")
# s='2', type(s)=<class 'str'>

l1 = [1, "2", 3, 4, 5]
random.shuffle(l1)
print(l1)
# ['2', 1, 5, 3, 4]

l2 = random.sample(['red', 'blue'], counts=[4, 2], k=5)
print(l2)

s1 = random.choices((1, "2", 3, 4, 5), k=2)
print(f"{s1=}, {type(s1)=}")
# s1=['2', 1], type(s1)=<class 'list'>

# -------------------- real-valued distributions  -------------------
# random.uniform(a, b)
# random.random()
```

