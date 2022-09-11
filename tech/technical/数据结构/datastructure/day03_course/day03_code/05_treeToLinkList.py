"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中节点指针的指向
思路:
  1.中序遍历,拿到递增序列
  2.依次遍历节点处理
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.li = []

    def tree_to_link(self, root):
        # 1.中序遍历
        # [Node(1),Node(2),Node(3),Node(4),Node(5)]
        li = self.mid_travel(root)
        # 特殊情况:空树 或 只有树根的树
        if not li or len(li) == 1:
            return root

        # 2.处理头尾节点
        li[0].left = None
        li[0].right = li[1]
        li[-1].left = li[-2]
        li[-1].right = None
        # 3.处理中间节点
        for index in range(1, len(li) - 1):
            li[index].left = li[index-1]
            li[index].right = li[index+1]

        # 思考:最终返回值: 双向链表的头节点
        return li[0]

    def mid_travel(self, root):
        if not root:
            return

        self.mid_travel(root.left)
        self.li.append(root)
        self.mid_travel(root.right)

        return self.li

if __name__ == '__main__':
    s = Solution()
    t12 = TreeNode(12)
    t5 = TreeNode(5)
    t18 = TreeNode(18)
    t2 = TreeNode(2)
    t9 = TreeNode(9)
    t15 = TreeNode(15)
    t19 = TreeNode(19)
    t17 = TreeNode(17)
    t16 = TreeNode(16)
    # 开始创建树
    t12.left = t5
    t12.right = t18
    t5.left = t2
    t5.right = t9
    t18.left = t15
    t18.right = t19
    t15.right = t17
    t17.left = t16
    # 测试方法
    h = s.tree_to_link(t12)
    while h:
        print(h.value, end=" ")
        h = h.right





















