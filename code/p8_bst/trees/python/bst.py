from tree_visualizer import TreeVisualizer
from tree_node import TreeNode

class BST:
    def __init__(self, root_value=None):
        if root_value is None:
            self.root = None
            return
        self.root = TreeNode(root_value)
        
    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.root == other.root

    def insert_node(self, value, current_node=None):
        if current_node is None:
            current_node = self.root
        if self.root is None:
            self.root = TreeNode(value)
            return
        if current_node.value > value:
            if current_node.left:
                self.insert_node(value, current_node.left)
            else:
                current_node.left = TreeNode(value)
        else:
            if current_node.right:
                self.insert_node(value, current_node.right)
            else:
                current_node.right = TreeNode(value)


    def insert_list(self, lst):
        for i in lst:
            self.insert_node(i)

    def visualize(self):
        TreeVisualizer.visualize(self.root)


    __dummy = 0xDEADBEEF

    def recursive_inorder_traverse(self, current_node=__dummy):
        if current_node == self.__dummy:
            current_node = self.root
        if current_node is None:
            return []
        return self.recursive_inorder_traverse(current_node.left) + \
            [current_node.value] \
            + self.recursive_inorder_traverse(current_node.right)

    def recursive_preorder_traverse(self, current_node=__dummy):
        if current_node == self.__dummy:
            current_node = self.root
        if current_node is None:
            return []
        return [current_node.value] + \
            self.recursive_preorder_traverse(current_node.left) + \
            self.recursive_preorder_traverse(current_node.right)


    def recursive_postorder_traverse(self, current_node=__dummy):
        if current_node == self.__dummy:
            current_node = self.root
        if current_node is None:
            return []
        return self.recursive_postorder_traverse(current_node.left) + \
            self.recursive_postorder_traverse(current_node.right) + \
            [current_node.value]