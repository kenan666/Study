# 路径总和
'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

'''
# 深度优先遍历
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root: 
        return False
    if not root.left and not root.right and sum - root.val == 0:
        return True
    return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


#路径总和2
'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

'''
#解 用DFS遍历时候,记录val
def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    res = []
    if not root: return []
    def helper(root,sum, tmp):
        if not root:
            return 
        if not root.left and not root.right and sum - root.val == 0 :
            tmp += [root.val]
            res.append(tmp)
            return 
        helper(root.left, sum - root.val, tmp + [root.val])
        helper(root.right, sum - root.val, tmp + [root.val])
    helper(root, sum, [])
    return res


# 二叉树展开为链表
'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''
# 解1 把树转换成列表，因为结果是按前序遍历排列的。
def flatten(self, root: TreeNode) -> None:
    
    if not root:return root
    d = []
    def helper(root):
        if not root:
            return 
        d.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    i = 1 
    root.left = None
    p = root
    while i < len(d):
        p.right = TreeNode(d[i])
        p = p.right
        i += 1

# 解2 递归。类似后序遍历
def flatten(self, root: TreeNode, pre = None) -> None:
    # 类似后序遍历
    def helper(root, pre):
        if not root: return pre
        # 记录遍历时候,该节点的前一个节点
        pre = helper(root.right, pre)
        pre = helper(root.left, pre)
        # 拼接
        root.right = pre
        root.left = None
        pre = root
        return pre
    helper(root, None)

#迭代
def flatten(self, root: TreeNode) -> None:
    cur = root
    while cur:
        if cur.left:
            p = cur.left
            while p.right: p = p.right
            p.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right

