"""
从上到下按层打印二叉树，同一层结点从左至右输出，每一层输出一行
思路:
  1.利用队列思想: append() + pop(0)
  2.一个队列存储当前层,一个队列存储下一层
    利用交换变量的思想
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def print_tree_layer(self, root):
        curq = [root]
        nextq = []
        # 打印当前层,添加下一层
        while curq:
            cur = curq.pop(0)
            print(cur.value, end=" ")
            # 左右孩子添加到下一层
            if cur.left:
                nextq.append(cur.left)
            if cur.right:
                nextq.append(cur.right)
            # 一定要判断,确保当前层打印完成,
            # 下一层添加完成,再交换变量
            if not curq:
                curq, nextq = nextq, curq
                # 打印空行
                print()

if __name__ == '__main__':
    s = Solution()
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p6 = Node(6)
    p7 = Node(7)
    p8 = Node(8)
    p9 = Node(9)
    p10 = Node(10)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    p4.left = p8
    p4.right = p9
    p5.left = p10

    s.print_tree_layer(p1)









