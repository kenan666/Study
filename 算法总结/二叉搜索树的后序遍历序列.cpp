/*
1--题目
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。是，返回true，否则返回false

例如  5,7,6,9,11,10,8  --》返回true  
          8
        6   10
       5 7 9   11
由图可知，后序遍历  5  7  6  9  11  10  8  是对应的二叉搜索树

***  二叉搜索树的概念
它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
                                           若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
                                           它的左、右子树也分别为二叉排序树。

分析：
1、后序遍历结果的最后一个数字 8 就是根节点值
2、在这个数组中，前 3 个数字 5  7  6  都比  8  小，是值为  8  的节点的左子树节点；
   后续三个数字 9  11  10  比 8  大，是右子树节点
3、利用相同的方法确定对应子树的结构，实际是 递归
   3.1 对于 5  7  6 ，最后数字6是左子树的根节点，数字 5 比6 小，是左子节点，7 比6 大，是右子节点
   3.2 对于 9  11  10 ， 最后数字 10 是右子树的根节点，数字 9 比10 小，是左子节点，11比10大，是右子节点

****####****
关键问题  1、 后序遍历如何遍历
         2、 二叉搜索树相关定义
*/

bool VerifySquenceOfBST(int sequence[],int length)
{
    if (sequence == nullptr || length <=0)
        return false;

    int root = sequence[length - 1];

    // 在二叉搜索树中左子树节点的值小于根节点的值
    int i = 0;
    for (; i < length -1; ++i)
    {
        if (sequence[i] > root)
            break;
    }

    // 在二叉搜索树中右子树节点的值大于根节点的值
    int j=i;
    for (;j < length -1; ++j)
    {
        if (sequence[j] < root)
            return false;
    }

    // 判断左子树是不是二叉搜索树
    bool left = true;
    if (i>0)
    {
        left = VerifySquenceOfBST(sequence,i);
    }

    //判断 右子树是不是二叉搜索树
    bool right = true;
    if (i<length - 1)
    {
        right = VerifySquenceOfBST(sequence+i,length-i-1);
    }
    return (left && right);
}
