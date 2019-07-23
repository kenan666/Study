'''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
3--->2--->0--->4
     |---------|
示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
1--->2
|----|

示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
1

'''
# 解1
# 哈希, 空间复杂度O(n)  把遍历过的节点记录,当发现遍历的节点下一个节点遍历过, 说明有环
def hasCycle(self, head):
    lookup = set()
    p = head
    while p:
        lookup.add(p)
        if p.next in lookup:
            return True
        p = p.next
    return False

# 解 2  快慢指针
def hasCycle(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False



'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
3--->2--->0--->4
     |---------|

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
1--->2
|----|

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
1

'''
# 解1 哈希，空间复杂度为O(n)  把遍历过的节点记录,当发现遍历的节点下一个节点遍历过, 返回它

def detectCycle(self, head):
   
    lookup = set()
    p = head
    while p:
        lookup.add(p)
        if p.next in lookup:
            return p.next
        p = p.next
    return None


# 解2 快慢指针
'''
算法思路:

1、先用快慢指针, 找到他们相遇点(如果存在环)
2、再重新从链表头开始, 以及步骤1的相遇点, 两个位置一起走, 再次相遇就是环的入口

证明：

          |--m-|         
          |---------|   环的周长：R
1--->2--->3--->4--->5
|----s----|

注意: 起始节点(head), 环的入口节点(输出结果), 相遇的节点(快慢指针求的)

我们要证明 : 初始点到环的入口的步数 等于 相遇点到环入口的步数

我们令, 初始点到入口为 s, 入口到相遇点 m, 环的周长为 r

我们只需证明: s == r - m

首先我们假设,慢指针走了 k 步到相遇点, 那么快指针就是 2k 步,所以我们有 2k - k = nr即 k = nr(慢指针还没到环,快指针已经转了好几圈)

还有, s = k - m

得 : s = nr - m ==> s == (n - 1) r + (r - m)

'''
def detectCycle(self, head):
    
    if not head or not head.next : return 
    # 快慢指针
    slow = head
    fast = head
    # 重新开始
    start = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # 找到相遇点
        if slow == fast:
            while slow != start:
                slow = slow.next
                start = start.next
            return slow
    return None
