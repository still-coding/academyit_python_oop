from bst import BST


bst = BST()
bst.insert_list([5, 2, 1, 3, 6, 4])
bst.visualize()


print("inorder", bst.recursive_inorder_traverse())
print("preorder", bst.recursive_preorder_traverse())
print("postorder", bst.recursive_postorder_traverse())
print("levelorder", bst.level_order_traverse())
