"""
python实现二叉树
"""
class Node:
    """节点类"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """初始化一棵空树"""
        self.root = None

    def add(self, item):
        """在二叉树中添加一个节点"""
        # 利用队列思想: append() + pop(0)
        node = Node(item)
        # 空树的情况
        if not self.root:
            self.root = node
            return
        # 非空树的情况
        q = [self.root]
        while True:
            cur = q.pop(0)
            # 判断左孩子
            if cur.left:
                q.append(cur.left)
            else:
                cur.left = node
                return
            # 判断右孩子
            if cur.right:
                q.append(cur.right)
            else:
                cur.right = node
                return

    def breadth_travel(self):
        """广度遍历:从上到下,从左到右"""
        q = [self.root]
        while q:
            cur = q.pop(0)
            print(cur.value, end=' ')
            # 判断左孩子
            if cur.left:
                q.append(cur.left)
            # 判断右孩子
            if cur.right:
                q.append(cur.right)




















