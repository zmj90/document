"""
python实现链式队列
思路:
    1.目标:队列(FIFO)
    2.设计:
      队尾: 链表尾部,负责入队
      队头: 链表头部,负责出队
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkQueue:
    def __init__(self):
        """初始化一个空队列"""
        self.head = None

    def enqueue(self, item):
        """入队:链表尾部添加一个节点"""
        node = Node(item)
        # 空队列
        if not self.head:
            self.head = node

        cur = self.head
        while cur.next:
            cur = cur.next
        # 循环结束: cur为尾节点
        cur.next = node
        node.next = None

    def dequeue(self):
        """出队:删除链表头节点"""
        if not self.head:
            raise Exception('dequeue from empty linkqueue')

        value = self.head.value
        self.head = self.head.next

        return value

if __name__ == '__main__':
    q = LinkQueue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    # 100 200 300 异常
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())



























