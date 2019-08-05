'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。


示例:
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


'''
# DFS 
# 可以根据前序遍历  前序 根--》左--》右 ，改变一下得到  根--》右--》左
def rightSideView(self, root: TreeNode) -> List[int]:
    def dfs(node, res, depth):
        if node is None:
            return
        if len(res) == depth:
            res.append(node.val)
        dfs(node.right, res, depth + 1)
        dfs(node.left, res, depth + 1)
    res = []
    dfs(root, res, 0)
    return res

# BFS
# 利用层次遍历
def rightSideView(self, root: TreeNode) -> List[int]:
    if root is None:
        return []

    res = []
    queue = [root]
    while queue:
        cur_size = len(queue)
        res.append(queue[-1].val)
        # 上一层的结点要全部出列
        for _ in range(cur_size):
            top = queue.pop(0)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
    return res
