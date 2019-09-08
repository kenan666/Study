'''
题目：链表中倒数第k个节点

题：输入一个链表，输出该链表中倒数第k个结点。
'''
'''
解题思路：为了实现只遍历链表一次就能找到倒数第k个节点，我们可以定义两个指针。

1、让第一个指针先向前走k-1步，第二个指针保持不动；
2、从第k步开始，第二个指针也开始从链表的头指针开始遍历。

由于两个指针的距离保持在k-1,当第一个指针到达链表的尾节点时，第二个指针刚好到达倒数第k个节点。
'''
# a 指针先走k-1。b指针跟着走（第k步开始时）
def findKthToTail(head ,k):
    if not head or k <= 0:
        return False
    
    pAhead = head
    pBehind = None

    for i in range (k - 1):
        if pAhead.next:
            pAhead = pAhead.next 
        else:
            return None

    pBehind = head
    while pAhead.next:
        pAhead = pAhead.next 
        pBehind = pBehind.next 

    return pBehind 

