#对称二叉树
'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

'''
# 解1 递归
def isSymmetric(self, root: TreeNode) -> bool:
    if not root: return True
    def Tree(p, q):
        if not p and not q: return True
        if p and q and p.val == q.val :
            return Tree(p.left, q.right) and Tree(p.right, q.left)     
        return False
    return Tree(root.left, root.right)

# 解 2  迭代
def isSymmetric(self, root: TreeNode) -> bool:
    if not root: return True
    def Tree(p, q):
        stack = [(q, p)]
        while stack:
            a, b = stack.pop()
            if not a and not b:
                continue
            if a and b and a.val == b.val:
                stack.append((a.left, b.right))
                stack.append((a.right,b.left))
            else:
                return False
        return True
    return Tree(root.left, root.right)

#二叉树的层次遍历
'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''
# 迭代
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    res = []
    cur_level = [root]
    while cur_level:
        tmp = []
        next_level = []
        for node in cur_level:
            tmp.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        res.append(tmp)
        cur_level = next_level
    return res

# 递归
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []
    
    def helper(root, depth):
        if not root: return 
        if len(res) == depth:
            res.append([])
        res[depth].append(root.val)
        helper(root.left, depth + 1)
        helper(root.right, depth + 1)
    helper(root, 0)
    return res


# 二叉树锯齿形层次遍历
'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''
# 解1 广度优先遍历
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    res = []
    cur_level = [root]
    depth = 0
    while cur_level:
        tmp = []
        next_level = []
        for node in cur_level:
            tmp.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if depth % 2 == 1:
            res.append(tmp[::-1])
        else:
            res.append(tmp)
        depth += 1
        cur_level = next_level
    return res

# 递归
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    res = []
    
    def helper(root, depth):
        if not root: return 
        if len(res) == depth:
            res.append([])
        if depth % 2 == 0:res[depth].append(root.val)
        else: res[depth].insert(0, root.val)
        helper(root.left, depth + 1)
        helper(root.right, depth + 1)
    helper(root, 0)
    return res


# 二叉树的最大深度
'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

'''
# 解1，深度优先遍历  DFS
'''
1、首先将根节点放入stack中。
2、从stack中取出第一个节点，并检验它是否为目标。
    ·如果找到目标，则结束搜寻并回传结果。
    ·否则将它某一个尚未检验过的直接子节点加入stack中。
3、复步骤2。
4、如果不存在未检测过的直接子节点。
    ·将上一级节点加入stack中。
    ·重复步骤2。
5、重复步骤4。
6、若stack为空，表示整张图都检查过了——亦即图中没有欲搜寻的目标。结束搜寻并回传“找不到目标”。
'''
def maxDepth(self, root: TreeNode) -> int:
    if not root:return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 广度优先遍历  BFS
'''
1、首先将根节点放入队列中。
2、从队列中取出第一个节点，并检验它是否为目标。
    ·如果找到目标，则结束搜索并回传结果。
    ·否则将它所有尚未检验过的直接子节点加入队列中。
3、若队列为空，表示整张图都检查过了——亦即图中没有欲搜索的目标。结束搜索并回传“找不到目标”。
4、重复步骤2
'''
def maxDepth(self, root: TreeNode) -> int:
    from collections import deque
    if not root: return 0
    queue = deque()
    queue.appendleft(root)
    res = 0
    while queue:
        #print(queue)
        res += 1
        n = len(queue)
        for _ in range(n):
            tmp = queue.pop()
            if tmp.left:
                queue.appendleft(tmp.left)
            if tmp.right:
                queue.appendleft(tmp.right)
    return res

# 从前序与中序遍历中构造二叉树
'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

'''
'''
前序遍历是 : 根->左->右;中序遍历是:左->根->右

所以我们可以通过前序遍历,可以把树分成左右部分.

例如示例中, 前序遍历3,那么节点3左右子树为[9];[15,20,7],然后我们递归下去

'''

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    loc = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1 : loc + 1], inorder[ : loc])
    root.right = self.buildTree(preorder[loc+1 : ], inorder[loc+1: ])
    return root


# 从后序与中序遍历中构造二叉树
'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

'''
'''
后序遍历是 : 左->右->根;中序遍历是:左->根->右

所以我们可以通过后序遍历,可以把树分成左右部分.

例如示例中, 后序遍历最后一个节点3,那么节点3左右子树为[9];[15,20,7],然后我们递归下去

'''
def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder: 
        return None
    root = TreeNode(postorder[-1])
    loc = inorder.index(postorder[-1])
    root.left = self.buildTree(inorder[ : loc], postorder[ :loc])
    root.right = self.buildTree(inorder[loc+1:], postorder[loc:-1])
    return root

# 二叉树的层次遍历2
'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

'''
# 递归
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    res = []
    def helper(root, depth):
        if not root: return 
        if depth == len(res):
            res.insert(0, [])
        res[-(depth+1)].append(root.val)
        helper(root.left, depth+1)
        helper(root.right, depth+1)
    helper(root, 0)
    return res

# 将有序数组转换成二叉搜索树
'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

'''
'''
找到数组的中点, 然后分成两部分,

比如[-10,-3,0,5,9], 节点0的左边[-10, -3],右边[5, 9]

依次递归下去.
'''
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums: 
        return 
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])
    return root


# 有序链表转换成二叉搜索树
'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

'''
# 找中点  ，链表中点，利用快慢指针寻找
def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findmid(head, tail):
        slow = head
        fast = head
        while fast != tail and fast.next!= tail :
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def helper(head, tail):
        if  head == tail: return 
        node = findmid(head, tail)
        root = TreeNode(node.val)
        root.left = helper(head, node)
        root.right = helper(node.next, tail)
        return root
        
    return helper(head, None)

# 平衡二叉树
'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

'''
# 自底向上
def isBalanced(self, root: TreeNode) -> bool:
    self.res = True
    def helper(root):
        if not root:
            return 0
        left = helper(root.left) + 1
        right = helper(root.right) + 1
        #print(right, left)
        if abs(right - left) > 1: 
            self.res = False
        return max(left, right)
    helper(root)
    return self.res

# 二叉树的最小深度
'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2

'''
# 判断叶子节点，然后取最小值
def minDepth(self, root: TreeNode) -> int:  
    if not root: return 0
    def helper(root):
        if not root: return float("inf")
        if not root.left and not root.right: return 1
        return min(helper(root.left), helper(root.right)) + 1
    return helper(root)
