'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

'''
# 解1 递归
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if not root:
            return 
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res

# 迭代
def inorderTraversal(self, root):
    
    res = []
    stack = []
    # 用p当做指针
    p = root
    while p or stack:
        # 把左子树压入栈中
        while p:
            stack.append(p)
            p = p.left
        # 输出 栈顶元素
        tmp = stack.pop()
        res.append(tmp.val)
        # 看右子树
        p = tmp.right
    return res



'''
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]

'''
# 解1  递归  依次输出根左右，递归进行
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if not root:
            return 
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return res

# 迭代 迭代:使用栈来完成,我们先将根节点放入栈中,然后将其弹出,依次将该弹出的节点的右节点,和左节点,**注意顺序,**是右,左,--栈是先入后出的,我们要先输出右节点,所以让它先进栈.
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]

'''

# 递归 左右根
def postorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if not root:
            return 
        helper(root.left)
        helper(root.right)
        res.append(root.val)
    helper(root)
    return res

# 迭代   改变入栈的顺序,刚才先序是从右到左,我们这次从左到右,最后得到的结果取逆
def postorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left :
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        res.append(node.val)
    return res[::-1]



'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

'''
# 递归  左根右
def inorderTraversal(self, root):
    
    res = []
    def helper(root):
        if not root:
            return 
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res

# 迭代
def inorderTraversal(self, root):
    
    res = []
    if not root:
        return res
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


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
# BFS  算法  广度优先遍历

'''
广度优先搜索算法（英语：Breadth-First-Search，缩写为BFS），又译作宽度优先搜索，或横向优先搜索，是一种图形搜索算法。
简单的说，BFS是从根节点开始，沿着树的宽度遍历树的节点。如果所有节点均被访问，则算法中止。

实现算法
1、首先将根节点放入队列中。
2、从队列中取出第一个节点，并检验它是否为目标。
 ·如果找到目标，则结束搜索并回传结果。
 ·否则将它所有尚未检验过的直接子节点加入队列中。
3、若队列为空，表示整张图都检查过了——亦即图中没有欲搜索的目标。结束搜索并回传“找不到目标”。
4、重复步骤2。

广度优先搜索算法能用来解决图论中的许多问题，例如：

查找图中所有连接组件（Connected Component）。一个连接组件是图中的最大相连子图。
查找连接组件中的所有节点。
查找非加权图中任两点的最短路径。
测试一图是否为二分图。

'''
def levelOrder(self, root):
    if not root:
        return []

    res.cur_level = [],[root]
    while cur_level:
        temp = []
        next_level = []
        for i in cur_level:
            temp.append(i.val)

            if i.left:
                next_level.append(i.left)

            if i.right:
                next_level.append(i.right)

        res.append(temp)
        cur_level = next_level
    return res


# 二叉搜索树
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
'''
递归
二叉搜索树, 一节点大于左子树节点, 小于右子树节点

所以我们节点是从1到n,当一个节点为val那么它的左边是<= val,右边是>=val,
'''
def generateTrees(self, n: int) -> List[TreeNode]:
    if n == 0: return []
    @functools.lru_cache(None)
    def helper(start, end):
        res = []
        if start > end:
            res.append(None)
        for val in range(start, end + 1):
            for left in helper(start, val - 1):
                for right in helper(val + 1, end):
                    root = TreeNode(val)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

    return helper(1, n)


# 不同的二叉搜索树
'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
'''
动态规划

假设n个节点存在

令G(n)的从1到n可以形成二叉排序树个数

令f(i)为以i为根的二叉搜索树的个数

即有:G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)

n为根节点，当i为根节点时，其左子树节点个数为[1,2,3,...,i-1]，右子树节点个数为[i+1,i+2,...n]，所以当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，即f(i) = G(i-1)*G(n-i),

上面两式可得:G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)

'''
def numTrees(self, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[-1]


# 验证二叉搜索树
'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

'''
#  因为二叉搜索树中序遍历是递增的,所以我们可以中序遍历判断前一数是否小于后一个数.
def isValidBST(self, root: TreeNode) -> bool:
    res = []
    def helper(root):
        if not root:
            return 
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res == sorted(res) and len(set(res)) == len(res)

# 恢复二叉搜索树
'''
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

'''

'''
这里我们二叉树搜索树的中序遍历(中序遍历遍历元素是递增的)

如下图所示, 中序遍历顺序是 4,2,3,1,我们只要找到节点4和节点1交换顺序即可!

这里我们有个规律发现这两个节点:

第一个节点,是第一个按照中序遍历时候前一个节点大于后一个节点,我们选取前一个节点,这里指节点4;

第二个节点,是在第一个节点找到之后, 后面出现前一个节点大于后一个节点,我们选择后一个节点,这里指节点1

               3
            /     \
           4       1
            \ 
             2
    
'''
# 迭代
def recoverTree(self, root: TreeNode) -> None:
    firstNode = None
    secondNode = None
    pre = TreeNode(float("-inf"))

    stack = []
    p = root
    while p or stack:
        while p:
            stack.append(p)
            p = p.left
        p = stack.pop()
        
        if not firstNode and pre.val > p.val:
                firstNode = pre
        if firstNode and pre.val > p.val:
            #print(firstNode.val,pre.val, p.val)
            secondNode = p
        pre = p
        p = p.right


# 相同的树
'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

'''
# 迭代
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    stack = [(q, p)]
    while stack:
        a, b = stack.pop()
        if not a and not b:
            continue
        if a and b and a.val == b.val:
            stack.append((a.left, b.left))
            stack.append((a.right,b.right))
        else:
            return False
    return True
