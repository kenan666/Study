# 二叉树前、中、后遍历

'''
给定一个二叉树，返回它的 前序、中序、后序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]

'''
#--------------------- 非递归------------------------
#思路
'''
对于二叉树中的任何一个节点而言，它都有两个角色需要扮演，一个是作为值存储的角色（角色1），另一个角色是作为它所带领的子树的一个代表（角色2）。
而我们设置的bool变量，就是为了说明我当前拿到的这个节点，应该是以一个值存储的这种角色对待它(True)，还是应该以一个子树的代表这种角色对待它（False），
如果是前者，那么就简单的将其所存储的值打印出来，如果是后者，我们需要继续探索由它带领的子树。

'''
#--------------前-------------------------
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    st=[(root,False)]
    res=[]
    while st:
        cur,vis=st.pop()
        if vis:
            res.append(cur.val)
        else:
            if cur.right:
                st.append((cur.right,False))
            if cur.left:
                st.append((cur.left,False))
            st.append((cur,True))
    return res

#--------------中-------------------------
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    st=[(root,False)]
    res=[]
    while st:
        cur,vis=st.pop()
        if vis:
            res.append(cur.val)
        else:
            if cur.right:
                st.append((cur.right,False))
            st.append((cur,True))
            if cur.left:
                st.append((cur.left,False))
    return res

#-------------后-------------------
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    st=[(root,False)]
    res=[]
    while st:
        cur,vis=st.pop()
        if vis:
            res.append(cur.val)
        else:
            st.append((cur,True))
            if cur.right:
                st.append((cur.right,False))
            if cur.left:
                st.append((cur.left,False))
    return res
