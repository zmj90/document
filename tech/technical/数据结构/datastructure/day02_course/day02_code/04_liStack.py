"""
python实现顺序栈模型
思路:
  1.目标:栈(LIFO)
  2.设计
    栈底:列表头部作为栈底,不进行任何操作
    栈顶:列表尾部作为栈顶,入栈和出栈操作
"""
class LiStack:
    def __init__(self):
        """初始化一个空栈"""
        self.elems = []

    def enstack(self, item):
        """入栈:相当于在列表尾部添加一个元素"""
        self.elems.append(item)

    def destack(self):
        """出栈:相当于弹出列表的最后一个元素"""
        # 空栈
        if not self.elems:
            raise Exception('destack from empty stack')

        return self.elems.pop()

if __name__ == '__main__':
    s = LiStack()
    s.enstack(100)
    s.enstack(200)
    s.enstack(300)
    # 300 200 100 异常
    print(s.destack())
    print(s.destack())
    print(s.destack())
    print(s.destack())




























