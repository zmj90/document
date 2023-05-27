import copy

l1 = [1, 2, 3, ["q", "w"]]

# 浅拷贝3种方式
l2 = l1[:]
l3 = l1.copy()
l4 = copy.copy(l1)
# 深拷贝
l5 = copy.deepcopy(l1)

l6 = l1

l1[3][0] = "4"
l1[0] = 111
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l1[0])
c = 1 + 2j
print(c)
