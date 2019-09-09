'''
题目：合并两个排序的链表

题：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解题思路：递归，并需注意对空链表单独处理。
'''
def mergeList(self,pHead1,pHead2):
    if not pHead1:
        return pHead2

    elif not pHead2:
        return pHead1

    pMergeHead = None

    if pHead1.val < pHead2.val :
        pMergeHead = pHead1
        pMergeHead.next = self.mergeList(pHead1.next ,pHead2)
    else:
        pMergeHead = pHead2
        pMergeHead.next = self.mergeList(pHead1,pHead2.next )

    return pMergeHead