'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''
#  交换左右子树的值，再递归左右子树。
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return 
    else:
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
    return root

#  时间复杂度 O(N)
#  空间复杂度O(logN)