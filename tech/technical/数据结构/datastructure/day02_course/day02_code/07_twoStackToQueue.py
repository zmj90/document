"""
用两个栈来实现一个队列，完成队列的 Push 和 Pop 操作。队列中的元素为 int 类型
分析:
    最终目标：队列(FIFO)-只要能保证先进去的元素先出来
    实现载体：两个栈(LIFO)-保证这两个栈中的元素是后进先出

    stacka: [] : append()+pop()
    stackb: [] : append()+pop()
"""
class Solution:
    def __init__(self):
        # 两个栈
        self.stacka = []
        self.stackb = []

    def push(self, item):
        """入队"""
        self.stacka.append(item)

    def spop(self):
        """出队"""
        # 先从stackb中出队
        if self.stackb:
            return self.stackb.pop()

        # 如果stackb为空,把stacka中元素添加到stackb中
        while self.stacka:
            self.stackb.append(self.stacka.pop())

        if self.stackb:
            return self.stackb.pop()

if __name__ == '__main__':
    # [100,200,300,400]
    s = Solution()
    s.push(100)
    s.push(200)
    print(s.spop())
    s.push(300)
    s.push(400)
    print(s.spop())
    print(s.spop())
    print(s.spop())






















