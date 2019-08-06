'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

'''
·遍历链表，在遍历的过程中更新两个指针pre, head：
    ·pre, head分别指向前一个Node和当前Node，每次执行head.next = pre
    ·nex用于提前保存下一个Node。
·由于需要返回新的链表头部，所以设置跳出条件为head.next == null,跳出后将最后head指向pre，并返回head。

'''
#-----迭代----------
def reverseList(self, head: ListNode) -> ListNode:
    if not head: return
    pre = None
    while head.next:
        nex = head.next
        head.next = pre
        pre = head
        head = nex
    head.next = pre
    return head

