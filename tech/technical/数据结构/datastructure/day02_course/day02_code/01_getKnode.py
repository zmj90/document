"""
输入一个链表，输出该链表中倒数第 k 个节点
思路：
  1.单链表,无法从尾到头遍历,只能从头到尾遍历
  2.按从头到尾顺序添加到一个列表中,利用列表的负向索引
"""
class Node:
    """节点类"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def get_k_node(self, head, k):
        cur = head
        li = []
        while cur:
            li.append(cur)
            cur = cur.next
        # 循环结束后,li中存放了所有节点对象
        if k > len(li):
            raise Exception('index out of range')

        return li[-k]

if __name__ == '__main__':
    s = Solution()
    # 创建链表: 100->200->300->None
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    # 测试方法
    print(s.get_k_node(head, 2).value)




















