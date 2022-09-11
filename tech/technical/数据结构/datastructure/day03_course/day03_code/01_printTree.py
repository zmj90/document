"""
之字形打印二叉树,要求：每层输出一行，奇数层从左至右，偶数层从右至左
思路:
    1.使用栈思想
    2.当前层奇数层: 添加下一层先左后右
      当前层偶数层: 添加下一层先右后左
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def print_tree(self, root):
        # 栈: append() + pop()
        curs = [root]
        nexts = []
        layer = 1
        while curs:
            node = curs.pop()
            print(node.value, end=" ")
            # 判断奇数层还是偶数层
            if layer % 2 == 1:
                if node.left:
                    nexts.append(node.left)
                if node.right:
                    nexts.append(node.right)
            else:
                if node.right:
                    nexts.append(node.right)
                if node.left:
                    nexts.append(node.left)
            # 判断是否需要交换变量
            if not curs:
                curs, nexts = nexts, curs
                print()
                layer += 1

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
    # 测试方法
    s.print_tree(p1)


























