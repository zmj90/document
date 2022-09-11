"""
输入两个链表，找出它们的第一个公共节点
思路:
    1.一旦有公共节点,则从第一个公共节点开始,后面全是公共节点
    2.从尾到头判断
"""
class Node:
    """节点工厂:节点类"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def first_public_node(self, head1, head2):
        cur1 = head1
        cur2 = head2
        li1 = []
        li2 = []
        # 将两个链表中所有节点对象添加到对应的列表中
        while cur1:
            li1.append(cur1)
            cur1 = cur1.next

        while cur2:
            li2.append(cur2)
            cur2 = cur2.next

        # 判断
        # li1:[Node(100),Node(200),Node(300),Node(400)]
        # li2:[Node(666),Node(300),Node(400)]
        node = None
        while True:
            if li1[-1] is li2[-1]:
                node = li1.pop()
                li2.pop()
            else:
                break

        return node

if __name__ == '__main__':
    s = Solution()
    n100 = Node(100)
    n200 = Node(200)
    n300 = Node(300)
    n400 = Node(400)
    n666 = Node(666)
    # 链表1:100->200->300->400->None
    n100.next = n200
    n200.next = n300
    n300.next = n400
    # 链表2:666->300->400->None
    n666.next = n300
    n300.next = n400
    # 测试方法: 300
    node = s.first_public_node(n100, n666)
    print(node.value)





























