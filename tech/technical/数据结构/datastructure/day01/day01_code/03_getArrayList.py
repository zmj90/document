"""
输入一个链表，按链表值从尾到头的顺序返回一个 ArrayList
"""
class Node:
    """节点类"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def get_array_list(self, head):
        array_list = []
        cur = head
        while cur:
            array_list.append(cur.value)
            cur = cur.next
        # 反转列表
        array_list.reverse()

        return array_list

if __name__ == '__main__':
    s = Solution()
    # 创建链表:100->200->300->None
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    # 测试方法:[300,200,100]
    print(s.get_array_list(head))


















