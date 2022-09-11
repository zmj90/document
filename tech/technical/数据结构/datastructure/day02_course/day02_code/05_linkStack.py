"""
python实现链式栈模型
思路:
  1.目标:栈(LIFO)
  2.设计
    栈顶:链表头部作为栈顶
        入栈:添加链表头节点
        出栈:删除链表头节点
    栈底:链表尾部作为栈底,入栈和出栈操作
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkStack:
    def __init__(self):
        """初始化一个空栈"""
        self.head = None

    def enstack(self, item):
        """入栈:添加链表头节点"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def destack(self):
        """出栈:删除链表头节点"""
        if not self.head:
            raise Exception('destack from empty stack')

        value = self.head.value
        self.head = self.head.next

        return value

if __name__ == '__main__':
    s = LinkStack()
    s.enstack(100)
    s.enstack(200)
    s.enstack(300)
    # 300 200 100 异常
    print(s.destack())
    print(s.destack())
    print(s.destack())
    print(s.destack())








