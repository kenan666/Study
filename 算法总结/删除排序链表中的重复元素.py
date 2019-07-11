'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

'''
# 思路一: 迭代 快慢指针,用快指针跳过那些有重复数组,慢指针负责和快指针拼接
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    dummy = ListNode(-1000)
    dummy.next = head
    slow = dummy
    fast = dummy.next
    while fast:
        if  fast.next and fast.next.val == fast.val:
            tmp = fast.val
            while fast and tmp == fast.val:
                fast = fast.next
        else:
            slow.next = fast
            slow = fast
            fast = fast.next
    slow.next = fast
    return dummy.next


# 递归
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:return head
    if head.next and head.val == head.next.val:
        while head.next != None and head.val == head.next.val:
            head = head.next
        return self.deleteDuplicates(head.next)
    else:
        head.next = self.deleteDuplicates(head.next)
    return head
