class TreeNode:
    def __init__(self, value, left=None, right=None):
        if not (left is None or isinstance(left, self.__class__)):
            raise TypeError("left must be a TreeNode or NoneType")
        if not (right is None or isinstance(right, self.__class__)):
            raise TypeError("right must be a TreeNode or NoneType")
        self.value = value
        self.left = left
        self.right = right

    
    def __str__(self):
        return f"({self.value}{f', l -> {self.left}' if self.left else ''}{f', r -> {self.right}' if self.right else ''})"


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.value != other.value:
            return False
        return self.left == other.left and self.right == other.right