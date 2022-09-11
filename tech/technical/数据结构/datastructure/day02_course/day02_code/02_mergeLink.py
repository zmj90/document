"""
输入两个单调递增的链表，输出两个链表合成后的链表
"""
class Node:
    """节点类"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def merge_link_list(self, head1, head2):
        # 1.确定新链表头节点
        h1 = head1
        h2 = head2
        if h1.value > h2.value:
            new_head = h2
            h2 = h2.next
        else:
            new_head = h1
            h1 = h1.next
        # 2.循环比较合并
        n = new_head
        while h1 and h2:
            if h1.value <= h2.value:
                # 三步操作
                n.next = h1
                h1 = h1.next
                n = n.next
            else:
                n.next = h2
                h2 = h2.next
                n = n.next
        # 循环结束:h1和h2一定有一个为None
        if h1:
            n.next = h1
        else:
            n.next = h2

        return new_head

if __name__ == '__main__':
    s = Solution()
    # 链表1: 100->200->300->None
    head1 = Node(100)
    head1.next = Node(200)
    head1.next.next = Node(300)
    # 链表2: 1->200->400->None
    head2 = Node(1)
    head2.next = Node(200)
    head2.next.next = Node(400)
    # 测试方法
    n = s.merge_link_list(head1, head2)
    # 打印新链表: 1 100 200 200 300 400
    while n:
        print(n.value, end=" ")
        n = n.next




















