# 1.计算n的阶乘
def fac(n):
    # 递归出口
    if n == 1:
        return 1

    return n * fac(n-1)

fac(4)

# 2. n+(n-1)+(n-2)+...+1的和
def s(n):
    if n == 1:
        return 1

    return n + s(n-1)

# python设定最大递归深度: 998
print(s(998))


def jump(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return jump(n-1) + jump(n-2)

print(jump(100))













