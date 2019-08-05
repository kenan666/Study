'''
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''
#  直接法
def removeElements(self, head, val):
    
    if head == None:
        return None
    
    while head is not None and head.val == val:
        head = head.next 
        
    if head == None:
        return None
    
    p = head
    
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    return head

#-----递归-------
def removeElements(self, head: ListNode, val: int) -> ListNode:
    if head: 
        head.next = self.removeElements(head.next, val)    
    return head.next if head and head.val == val else head
    
# 递归：每次都返回从当前位置算起第一个有效的节点或None
#-------------------
#--------迭代-------
def removeElements(self, head: ListNode, val: int) -> ListNode:
    while head and head.val == val:  # 用于找到应该返回的链表头（应该跳过所有特殊 val 的节点）
        head = head.next
    pre, cur = head, head and head.next
    while cur:   # 用于把前一个节点指针接到下一个节点（如果当前节点值为 val）
        if cur.val == val:
            pre.next = cur = cur.next
        else:
            pre, cur = cur, cur.next
    return head
