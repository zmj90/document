"""
python实现单链表
设计:
    1.数学模型:单链表
    2.设计一组操作
      is_empty(): 判断是否为空链表
      add(item): 在链表头部添加一个节点
      append(item):在链表尾部添加一个节点
      travel():遍历整个链表
      remove(item):移除某个节点
      insert(pos,item):在指定索引位置添加节点
"""
class Node:
    """节点类"""
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkList:
    """单链表的类"""
    def __init__(self):
        """初始化一个空链表"""
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def add(self, item):
        """在链表头部添加一个节点"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """在链表尾部添加一个节点"""
        cur = self.head
        node = Node(item)
        # 情况1:空链表情况
        if not self.head:
            self.add(item)
            return

        # 情况2:非空链表情况
        # 1.移动游标,找到尾节点
        while cur.next:
            cur = cur.next

        # 循环结束后,cur指向尾节点的位置
        # 2.添加节点
        cur.next = node
        node.next = None

    def travel(self):
        """遍历链表中所有节点"""
        cur = self.head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        # 打印空行
        print()

    def remove(self, item):
        """删除链表中的某个节点"""
        pre = None
        cur = self.head
        # 空链表情况
        if not self.head:
            raise Exception('remove item from empty linklist')
        # 删除头节点情况
        if cur.value == item:
            self.head = self.head.next
            return

        # 第一步:判断移动两个游标
        while cur:
            if cur.value != item:
                # 未找到删除的节点的情况
                pre = cur
                cur = cur.next
            else:
                # 删除成功
                pre.next = cur.next
                return

    def insert(self, pos, item):
        """在指定索引值(pos)添加一个节点"""
        # pos:从0开始,参照列表的insert()方法
        pass


if __name__ == '__main__':
    s = SingleLinkList()
    # 链表: 100 -> 200 -> 300 -> 400 -> None
    s.add(300)
    s.add(200)
    s.add(100)
    s.append(400)
    # 终端1: False
    print(s.is_empty())
    # 终端2: 100 200 300 400
    s.travel()
    s.remove(800)
    # 终端3: 200 300 400
    s.travel()





























