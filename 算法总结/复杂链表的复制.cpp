/*
题目： 实现 函数 ComplexListNode * Clone(ComplexListNode * pHead), 复制一个复杂链表。  在复杂链表中，每一个节点除了 有一个m_pNext指针
指向下一个节点，还有一个m_Sibling 指针指向链表中的任意节点或者nullptr。
定义结构如下：
struct ComplexListNode
{
    int m_nValue;
    ComplexListNode * pNext;
    ComplexListNode * pSibling;
};

实现方法：
第一种：
    第一步：复制原始链表上的每个节点，并用m_pNext连接起来，第二步：设置每个节点的m_pSibling指向节点 S  ，由于 S  在链表中可能在 N 前面也可能在 N 的
后面，所以定位 S 的位置需要从原始  链表的头结点开始找。  --》如果从原始链表的头结点开始沿着m_pNext  经过 s 步 找到 S ，那么在复制链表上节点  N`
的m_pSibling（记为  S`）离复制链表的头节点 的距离也沿着 m_pNext 指针 s 步。---》》》用这种方法就可以复制链表上的每个节点设置m_pSiblinhg 指针。

对于一个含有  n  个节点的链表，由于定位 每个节点的m_pSibling  都需要从链表头节点开始经过O（n）步才能找到，所以时间复杂度是O（n^2）

第二种：优化：
第一步：仍然复制原始链表上的每个节点 N  去创建  N`， 然后把这些创建好的节点  m_pNext  连接器来，同时 我们吧<N， N`>  的配对信息放到一个哈希表中；
第二步：设置复制链表上每个节点m_pSibling。  如果原始链表中  节点  N  的 m_pSibling  指向  S ，那么复制链表中，  N`  应该指向 S` ，由于利用
hash表，可以用O(1)的时间根据  S  找到  S`。

注：用空间换时间。  对于有  n 个节点的链表，  我们需要一个  O(n) 的hash表， 
    ---》》利用以O(n)的空间消耗，把时间复杂度由  O(n^2)  降低到O(n)
    
*/

//  ----->>  第三种：
/*
第一步：  在不用辅助空间的情况下，实现 O(n)的时间效率。
    ---》 根据链表的每个节点  N 创建对应的  N` ,并把  N` 连接到  N  的后面。
*/
void CloneNodes (ComplexListNode * pHead)
{
    ComplexListNode * pNode = pHead;
    while(pNode != nullptr)
    {
        ComplexListNode * pCloned = new ComplexListNode();
        pCloned->m_nValue = pNode->m_nValue;
        pCloned->m_pNext = pNode->m_pNext;
        pCloned->m_pSibling = nullptr;

        pNode->m_pNext = pCloned;

        pNode = pCloned->m_pNext;

    }
}

/*
第二步:  设置复制出来的节点的  m_pSibling  假设  原始链表上的  N  的m_pSibling  指向节点  S  ，那么对应复制出来的  N`  是  N 的m_pNext指向的节点
同样  S`  也是  S  的m_pNext  指向的节点
*/
void ConnectSiblingNodes(ComplexListNode * pHead)
{
    ComplexListNode * pNode = pHead;
    while (pNode != nullptr)
    {
        ComplexListNode * pCloned = pNode->m_pNext;
        if (pNode->m_pSibling != nullptr)
        {
            pCloned->m_pSibling = pNode->m_pSibling->m_pNext;
        }
        pNode = pCloned->m_pNext;
    }
}

/*
第三步：  把  长链表拆分成两个链表，
---》  奇数位置的节点用m_pNext  链接起来就是原始链表
---》  偶数位置节点用m_pNext链接起来就是复制链表
*/
ComplexListNode * ReconnectNodes(ComplexListNode * pHead)
{
    ComplexListNode * pNode = pHead;
    ComplexListNode * pClonedHead = nullptr;
    ComplexListNode * pClonedNode = nullptr;

    if (pNode != nullptr)
    {
        pClonedHead = pClonedHead = pNode->m_pNext;
        pNode->m_pNext = pClonedNode->m_pNext;
        pNode = pNode->m_pNext
    }

    while( pNode != nullptr)
    {
        pClonedNode->m_pNext = pNode->m_pNext;
        pClonedNode = pClonedNode->m_pNext;
        pNode->m_pNext = pClonedNode->m_pNext;
        pNode = pNode->m_pNext;
    }
    return pClonedHead;
}

//  整合上面三个步骤
ComplexListNode * Clone(ComplexListNode * pHead)
{
    CloneNodes(pHead);
    ConnectSiblingNodes(pHead);
    return ReconnectNodes(pHead)
}