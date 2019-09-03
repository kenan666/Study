'''
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
'''
思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
'''
def construct_tree(preorder=None, inorder=None):
    if not preorder or not inorder:
        return None

    index = inorder.index(preorder[0])  # 确定 根节点-->给定数据的第一个数字
    left = inorder[0:index]  # 左子树 所有节点
    right  = inorder[index+1:] # 右子树所有节点
    root = TreeNode (preorder[0])  # 根节点

    root.left = construct_tree(preorder[1:1+len(left)],left)
    root.right = construct_tree(preorder[-len(right):],right)

    return root
