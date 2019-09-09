'''
题：输入一个链表，反转链表并输出反转后链表的头节点。
'''
#------------思路-----------
'''
定义3个指针，分别指向当前遍历到的节点pNode、它的前一个节点pPrev及后一个节点pNext。
'''
def reverseList(pHead):
    pReverseHead = None
    pNode = pHead
    pPrev = None

    while pNode:
        pNext = pNode.next 
        if not pNext:
            pReverseHead = pNode

        pNode.next = pPrev
        pPrev = pNode
        pNode = pNext

    return pReverseHead