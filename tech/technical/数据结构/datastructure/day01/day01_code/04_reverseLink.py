"""
输入一个链表，反转链表后，输出新链表的表头
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse_link_list(self, head):
        cur = head
        pre = None
        while cur:
            # 记录下一个要反转的节点
            next_node = cur.next
            # 开始反转cur节点
            cur.next = pre
            pre = cur
            cur = next_node

        # 循环结束后,pre就为新链表的头节点
        return pre

if __name__ == '__main__':
    s = Solution()
    # 创建链表:100->200->300->None
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    # 测试方法
    h = s.reverse_link_list(head)
    while h:
        print(h.value, end=" ")
        h = h.next

















