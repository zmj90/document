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

    def pre_travel(self, root):
        """前序遍历: 根左右"""
        # 递归出口
        if not root:
            return

        print(root.value, end=" ")
        self.pre_travel(root.left)
        self.pre_travel(root.right)

    def mid_travel(self, root):
        """中序遍历: 左根右"""
        # 递归出口
        if not root:
            return

        self.mid_travel(root.left)
        print(root.value, end=" ")
        self.mid_travel(root.right)

    def rear_travel(self, root):
        """后序遍历: 左右根"""
        # 递归出口
        if not root:
            return

        self.rear_travel(root.left)
        self.rear_travel(root.right)
        print(root.value, end=" ")


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    # 终端1: 1 2 3 4 5 6 7 8 9 10
    tree.breadth_travel()
    print()
    tree.pre_travel(tree.root)
    print()
    tree.mid_travel(tree.root)
    print()
    tree.rear_travel(tree.root)
    print()



















