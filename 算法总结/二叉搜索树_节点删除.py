'''
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

'''
#----------二叉搜索树 知识点--------
'''
二叉查找树（Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）或排序二叉树（sorted binary tree），
是指一棵空树或者具有下列性质的二叉树：

    1、若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
    2、若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
    3、任意节点的左、右子树也分别为二叉查找树；
    4、没有键值相等的节点。

插入、删除、查找时间复杂度为 O(logN)  * 最坏 O(n)
'''
# ------二叉搜索树 查找------
'''
在二叉搜索树b中查找x的过程为：

    1、若b是空树，则搜索失败，否则：
    2、若x等于b的根节点的数据域之值，则查找成功；否则：
    3、若x小于b的根节点的数据域之值，则搜索左子树；否则：
    4、查找右子树。
    
'''
#---------------------------------------

# Status SearchBST(BiTree T, KeyType key, BiTree f, BiTree &p) {
#     // 在根指针T所指二元查找樹中递归地查找其關键字等於key的數據元素，若查找成功，
#     // 則指针p指向該數據元素節點，并返回TRUE，否則指针指向查找路徑上訪問的最後
#     // 一個節點并返回FALSE，指针f指向T的雙親，其初始调用值為NULL
#     if (!T) { // 查找不成功
#         p = f;
#         return false;
#     } else if (key == T->data.key) { // 查找成功
#         p = T;
#         return true;
#     } else if (key < T->data.key) // 在左子樹中繼續查找
#         return SearchBST(T->lchild, key, T, p);
#     else // 在右子樹中繼續查找
#         return SearchBST(T->rchild, key, T, p);
# }

#---------------------------------------

#---------二叉搜索树 节点插入------------
'''
向一个二叉搜索树b中插入一个节点s的算法，过程为：

    1、若b是空树，则将s所指节点作为根节点插入，否则：
    2、若s->data等于b的根节点的数据域之值，则返回，否则：
    3、若s->data小于b的根节点的数据域之值，则把s所指节点插入到左子树中，否则：
    4、把s所指节点插入到右子树中。（新插入节点总是叶子节点）
'''
#---------------------------------------------------

# /* 当二元搜尋樹T中不存在关键字等于e.key的数据元素时，插入e并返回TRUE，否则返回 FALSE */
# Status InsertBST(BiTree *T, ElemType e) {
#     if (!T) {
#         s = new BiTNode;
#         s->data = e;
#         s->lchild = s->rchild = NULL;
#         T = s; // 被插節点*s为新的根结点
#     } else if (e.key == T->data.key)
#         return false;// 关键字等于e.key的数据元素，返回錯誤
#     if (e.key < T->data.key)
#         InsertBST(T->lchild, e);  // 將 e 插入左子樹
#     else
#         InsertBST(T->rchild, e);  // 將 e 插入右子樹
#     return true;
# }

#---------------------------------------------------

#----------二叉搜索树 节点删除--------------
'''
在二叉查找树删去一个结点，分三种情况讨论：

    1、若*p结点为叶子结点，即PL（左子树）和PR（右子树）均为空树。由于删去叶子结点不破坏整棵树的结构，则只需修改其双亲结点的指针即可。

    2、若*p结点只有左子树PL或右子树PR，此时只要令PL或PR直接成为其双亲结点*f的左子树（当*p是左子树）或右子树（当*p是右子树）即可，作此修改也不破坏二叉查找树的特性。

    3、若*p结点的左子树和右子树均不空。在删去*p之后，为保持其它元素之间的相对位置不变，可按中序遍历保持有序进行调整，
       可以有两种做法：其一是令*p的左子树为*f的左/右（依*p是*f的左子树还是右子树而定）子树，*s为*p左子树的最右下的结点，
       而*p的右子树为*s的右子树；其二是令*p的直接前驱（in-order predecessor）或直接后继（in-order successor）替代*p，
       然后再从二叉查找树中删去它的直接前驱（或直接后继）。
'''
#------ C++ 版本-------------------------------------

# Status DeleteBST(BiTree *T, KeyType key) {
#     // 若二叉查找树T中存在关键字等于key的数据元素时，则删除该数据元素，并返回
#     // TRUE；否则返回FALSE
#     if (!T)
#         return false; //不存在关键字等于key的数据元素
#     else {
#         if (key == T->data.key)   //   找到关键字等于key的数据元素
#             return Delete(T);
#         else if (key < T->data.key)
#             return DeleteBST(T->lchild, key);
#         else
#             return DeleteBST(T->rchild, key);
#     }
# }

# Status Delete(BiTree *&p) {
#     // 该节点为叶子节点，直接删除
#     BiTree *q, *s;
#     if (!p->rchild && !p->lchild) {
#         delete p;
#         p = NULL;  // Status Delete(BiTree *&p) 要加&才能使P指向NULL
#     } else if (!p->rchild) { // 右子树空则只需重接它的左子树
#         q = p->lchild;
#         /*
#         p->data = p->lchild->data;
#         p->lchild=p->lchild->lchild;
#         p->rchild=p->lchild->rchild;
#         */
#         p->data = q->data;
#         p->lchild = q->lchild;
#         p->rchild = q->rchild;
#         delete q;
#     } else if (!p->lchild) { // 左子树空只需重接它的右子树
#         q = p->rchild;
#         /*
#         p->data = p->rchild->data;
#         p->lchild=p->rchild->lchild;
#         p->rchild=p->rchild->rchild;
#         */
#         p->data = q->data;
#         p->lchild = q->lchild;
#         p->rchild = q->rchild;
#         delete q;
#     } else { // 左右子树均不空
#         q = p;
#         s = p->lchild;
#         while (s->rchild) {
#             q = s;
#             s = s->rchild;
#         } // 转左，然后向右到尽头
#         p->data = s->data;  // s指向被删结点的“前驱”
#         if (q != p)
#             q->rchild = s->lchild;  // 重接*q的右子树
#         else
#             q->lchild = s->lchild;  // 重接*q的左子树
#         delete s;
#     }
#     return true;
# }

#-------------------------------------------

#---  python版本  -----------------------------------------

def find_min(self):   # Gets minimum node (leftmost leaf) in a subtree
    current_node = self
    while current_node.left_child:
        current_node = current_node.left_child
    return current_node

def replace_node_in_parent(self, new_value=None):
    if self.parent:
        if self == self.parent.left_child:
            self.parent.left_child = new_value
        else:
            self.parent.right_child = new_value
    if new_value:
        new_value.parent = self.parent

def binary_tree_delete(self, key):
    if key < self.key:
        self.left_child.binary_tree_delete(key)
    elif key > self.key:
        self.right_child.binary_tree_delete(key)
    else: # delete the key here
        if self.left_child and self.right_child: # if both children are present
            successor = self.right_child.find_min()
            self.key = successor.key
            successor.binary_tree_delete(successor.key)
        elif self.left_child:   # if the node has only a *left* child
            self.replace_node_in_parent(self.left_child)
        elif self.right_child:  # if the node has only a *right* child
            self.replace_node_in_parent(self.right_child)
        else: # this node has no children
            self.replace_node_in_parent(None)

#-----------------------------------------

# ----------二叉树遍历---------------
# 中序遍历(in-order traversal) 
def traverse_binary_tree(node, callback):
    if node is None:
        return
    traverse_binary_tree(node.leftChild, callback)
    callback(node.value)
    traverse_binary_tree(node.rightChild, callback)

#---------------------------------------------------------------------------------

# --- 题解----------
'''
删除某一节点的情况有三种：

1.该节点无子节点

2.该节点只有一个子节点

3.该节点有两个字节点
'''
'''
理解这个算法的关键在于保持 BST 中序遍历的顺序性，当待删除结点的左右结点都不为空的时候，让待删除结点的前驱结点或者后继结点代替被删除结点，
这样就能成为一棵树，并且还是 BST，否则就变成森林，或者不保持 BST 中序遍历的顺序性了。

**  第一种情况----待删除节点的的左子树为空
                 5                                                        5
              /    \                                                   /     \    
             1      6         -----> 删除 6 节点  ------>              1       8              --->  此时用 待删除 节点的 右子树 代替 6 就可以 
              \      \                                                 \     /  \  
               3      8                                                 3   7    9
              / \    / \                                               / \
             2   4  7   9                                             2   4
                                                                       


**  第二种情况-----待删除节点的右子树为空
             5                                                             5
            / \                                                           / \
           4   6                                                         2   6             ---> 此时用 待删除 节点的 左子树 代替 4 就可以 
          /                  -----> 删除 4 节点 ------->                 / \
         2                                                             1   3
        / \                                                                 
       1   3         

**  第三种情况-------  如果 待删除 节点的 左右子树 均不为空  ---> 处理方式1： 此时用 待删除 节点的 前驱节点 代替它
                   4                                                               4                                
                 /   \                                                           /   \                                          
                2     8                                                         2     7                     
               / \   / \              ----> 删除 节点 8 ---->                   / \   / \         ---> 此时用 待删除 节点的 前驱节点 代替 8 就可以                                 
              1   3 6   10                                                     1  3  6  10                 
                   / \  / \                                                         /   / \                         
                  5  7 9   11                                                      5   9   11
              * 节点 7 是 节点 8 的 前驱节点     

**  第三种情况-------  如果 待删除 节点的 左右子树 均不为空  ---> 处理方式2： 此时用 待删除 节点的 后继节点 代替它
                   4                                                               4                                
                 /   \                                                           /   \                                          
                2     8                                                         2     9                     
               / \   / \              ----> 删除 节点 8 ---->                   / \   / \         ---> 此时用 待删除 节点的 后继节点 代替 8 就可以                                 
              1   3 6   10                                                     1  3  6  10                 
                   / \  / \                                                         / \   \                         
                  5  7 9   11                                                      5   7   11
              * 节点 9 是 节点 8 的 后继节点                                                                         
'''

#-----------解1--- 前驱节点 代替被删除节点----------
# 方法1：用左子树中最大结点的代替被删除结点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.left is None:
            new_root = root.right
            root.right = None
            return new_root

        if root.right is None:
            new_root = root.left
            root.left = None
            return new_root

        # 找到左子树中最大的
        predecessor = self.__maximum(root.left)
        predecessor_copy = TreeNode(predecessor.val)
        predecessor_copy.left = self.__remove_max(root.left)
        predecessor_copy.right = root.right
        root.left = None
        root.right = None
        return predecessor_copy

    def __remove_max(self, node):
        if node.right is None:
            new_root = node.left
            node.left = None
            return new_root
        node.right = self.__remove_max(node.right)
        return node

    def __maximum(self, node):
        while node.right:
            node = node.right
        return node

#------解2 --- 后继节点代替被删除节点------
# 方法2：用右子树中最小结点的代替被删除结点
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.left is None:
            new_root = root.right
            root.right = None
            return new_root

        if root.right is None:
            new_root = root.left
            root.left = None
            return new_root

        # 找到右子树中最小的结点，复制它的值
        successor = self.__minimum(root.right)
        successor_copy = TreeNode(successor.val)
        successor_copy.left = root.left
        successor_copy.right = self.__remove_min(root.right)
        root.left = None
        root.right = None
        return successor_copy

    def __remove_min(self, node):
        if node.left is None:
            new_root = node.right
            node.right = None
            return new_root
        node.left = self.__remove_min(node.left)
        return node

    def __minimum(self, node):
        while node.left:
            node = node.left
        return node

#-----------------参考其他解-------------------
# ----  递归求解-----------
def deleteNode(self, root, key):

    if not root: return None;
    if root.val > key:
        root.left = self.deleteNode(root.left, key)
    elif root.val < key:
        root.right = self.deleteNode(root.right, key)
    else:
        if not root.left or not root.right:
            root = root.left if root.left else root.right
        else:
            cur = root.right
            while cur.left: cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        
    return root

# -----  解 2 --- 参考 ---
def deleteNode(self, root, key):
    
    def deleteNode_c(root):
        # 删除root中值为key的节点，并返回根结点
        if root is None:
            return None
        if root.val == key:
            # 如果没有左子树和右子树，删除自己
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # 使用右边最小值替换掉当前节点，然后删除右子树的最小值
                p = find_min_c(root.right)
                root.right = delete_min_c(root.right)
                p.left = root.left
                p.right = root.right
                return p

        elif root.val > key:
            # 去左子树中删除，并把自己的left指向删除后的左子树
            root.left = deleteNode_c(root.left)
            return root
        else:
            root.right = deleteNode_c(root.right)
            return root

    def find_min_c(root):
        if root is None:
            return root
        p = root
        while p.left is not None:
            p = p.left
        return p

    def delete_min_c(root):
        # 删除root为根节点的树中的最小值
        if root is None:
            return None
        elif root.left is None:
            # 此时为要删除的节点
            return root.right
        else:

            root.left = delete_min_c(root.left)
            return root
    return deleteNode_c(root)