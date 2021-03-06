'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5


'''
'''
思路一：
用栈，我们把 k 个数压入栈中，然后弹出来的顺序就是翻转的！

这里要注意几个问题：

第一，剩下的链表个数够不够 k 个（因为不够 k 个不用翻转）；

第二，已经翻转的部分要与剩下链表连接起来

'''
#  解1
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    p = dummy

    while True:
        count = k
        stack = []
        tmp = head
        while count and tmp :
            stack.append(tmp)
            tmp = tmp.next
            count -= 1

        # 目前tmp在k+1位置
        # 说明剩下的链表不够k个，跳出循环
        if count:
            p.next = head
            break
        
        # 翻转操作
        while stack:
            p.next = stack.pop()
            p = p.next 

        p.next = tmp
        head = tmp

    return dummy.next 


'''
尾插法

直接举个例子：k = 3

pre
tail    head
dummy    1     2     3     4     5
# 我们用tail 移到要翻转的部分最后一个元素
pre     head       tail
dummy    1     2     3     4     5
	          cur
# 我们尾插法的意思就是,依次把cur移到tail后面
pre          tail  head
dummy    2     3    1     4     5
	    cur
# 依次类推
pre     tail      head
dummy    3     2    1     4     5
		      cur

'''
# 解2 尾插法
def reverseKGroup(self, head: ListNode, k: int) -> ListNode :
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    tail = dummy
    while True:
        count = k
        while count and tail:
            count -= 1 
            tail = tail.next

        if not tail :
            break
        
        head = pre.next 
        while pre.next !=tail:
            cur = pre.next   #  获取下一元素
            # pre 与cur.next 连接起来 此时，cur掉了出来
            pre.next = cur.next
            cur.next = tail.next  #  将剩余的链表连接起来
            tail.next = cur  #  插在tail后面

        # 改变  pre tail 的值
        pre = head
        tail = head 
    return dummy.next  

#  解3  递归
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count!= k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur   
        return head

