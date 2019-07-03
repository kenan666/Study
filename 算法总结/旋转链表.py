'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

'''
'''
示例1,1->2->3->4->5->NULL, k = 2 ,我们要找到3这个值,只要把它下一位为空,将下面一段链表和它这段链表连接起来
1->2->3->4->5->NULL  ---> 1->2->3->NULL    ---> 4->5->1->2->3->NULL
                          4->5->NULL     

题目的意思是向右移动2位,换句话说, 以3作为链表头,把它前面的链表连在它后面!现在问题就是如何找3,我们发现链表的个数-k就是从链表头到3位置.

还有一个问题,就是如果k = 6其实就是相等于k=1;所以我们要防止循环.

问题变成了,1. 求链表长度;2. 找 num - num % k的位置

'''
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or not head.next or not k: return head
    num = 0
    dummy = ListNode(0)
    dummy.next = head
    p1 = dummy
    p2 = dummy
    # 计算个数
    while p1.next:
        num += 1
        p1 = p1.next
    #print(num)
    # 找前一段链表
    k = num - k % num
    #print(k)
    while k :
        p2 = p2.next
        k -= 1
    
    # 连接
    p1.next = dummy.next
    dummy.next = p2.next
    p2.next = None
    
    return dummy.next
