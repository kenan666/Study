/*
题目： 出入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶子节点所经过的节点形成一条路径。



分析：  例如输入一下二叉树和整数 22 ，则打印出路径为两条，第一条包含路径  10  12  ，第二条包含路径  10  5  7
       10
    5      12
  4   7

1、路径从根节点出发--》到叶子节点  --》》根节点为起始节点 ---》》 在遍历二叉树的时候，之后  先序遍历 是从根节点开始访问，所以  方法是利用先序遍历
2、上述二叉树中  ，在访问节点 10  之后 ，访问节点 5 ，在题目中没有出现   父节点指针， 当访问节点  5  的时候，  不知道 前面经历了哪些节点，
   除非把经过的节点保存下来，没访问一个节点，把当前节点添加到路径中去。  
   ---》 此时访问5  时，路径中包含两个节点，分别为  10、 5，接下来访问  4 ，把 4 添加到路径中。
   --》此时已经达到叶节点，但路径上三个值的和不等于输入整数22，因此不是符合要求的路径。
3、接下来遍历其他节点。在遍历下一个节点之前，先返回节点  5 ，再去遍历  右子节点  7 ，
   ---》在返回节点 5  的时候 ， 节点 4  已经不在路径中，  删除  节点 4  
   ---》访问  节点 7  的时候，把  节点  7  添加到路径中 
   ---》得到  路径  10  5  7  ，是一条符合要求的路径
4、最后遍历节点 12 ，
   ---》 遍历之前，先回到节点 10 ，先删除其他子节点，
   ---》 最后遍历节点 12 ，是一条符合要求的路径

步骤：          操作              是否叶节点                    路径                             路径节点值的和
1            访问节点10               否                    节点10                                  10 
2            访问节点5                否                    节点10、节点5                            15
3           访问节点4                 是                    节点10、节点5、节点4                      19
4            返回节点5                                      节点10、节点5                            15
5           访问节点7                 是                     节点10、节点5 、节点7                     22
6           返回节点5                                        节点10、节点5                           15
7           返回节点10                否                     节点10                                  10
8           访问节点 12               是                     节点10、节点12                           22

小结：
1、当用前序遍历访问到某一节点时，把该节点添加到路径上，并累加该节点的值
    --》如果是叶子节点，并且路径中节点的值和输入的整数值相等，则路径符合要求并打印出路径
    --》如果不是叶子节点，则继续访问叶子节点。
    --》因此在函数退出之前，要在路径上删除当前节点并减去当前节点的值，以确保返回父节点时路径刚好是从根节点到父节点。
2、算法数据结构用的是  栈  ， ，
*/
//  参考代码

//二叉树节点定义如下：
struct BinaryTreeNode
{
    int m_nValue;
    BinaryTreeNode  * m_pLeft;
    BinaryTreeNode  * m_pRight;
}

void FindPath(BinaryTreeNode *pNode,int exceptedSum)
{
    if (pRoot == nullptr)
        return ;
    std::vector< int >path;
    int currentSum = 0;
    FindPath(pRoot,exceptedSum,currentSum);
}

void FindPath(BinaryTreeNode * pRoot,int exceptedSum,int currentSum,std::vector<int>&path)
{
    currentSum += pRoot->m_nValue;
    path.push_back(pRoot->m_nValue);

    //如果是叶节点，并且路径上节点值等于输入的值，--》打印出这条路径
    bool isLeaf = pRoot->m_pLeft == nullptr && pRoot->m_pRight == nullptr;
    if (currentSum == exceptedSum && isLeaf)
    {
        print("A path is found :");
        std::vecyor<int>::iterator iter = path.begin();
        for (; iter!=path.end(); ++iter)
            print("%d\t",*iter);
        print("\n");
    }

    //如果不是叶子节点，则遍历它的叶节点
    if (pRoot->m_pLeft != nullptr)
        FindPath(pRoot->m_pLeft,exceptedSum,currentSum);
    if (pRoot->m_pRight != nullptr)
        FindPath(pRoot->m_pRight,exceptedSum,currentSum);
    
    //返回父节点之前，在路径上删除当前节点
    path.pop_back();
}