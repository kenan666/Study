'''
题目：如果一个链表中包含环，如何找出环的入口节点？
'''
# -----解析---------
'''
解题分析：其实此题可以分解为三个题目：
1）如何判断一个链表中是否包含环？
2）如何找到环的入口节点？
3）如何得到环中节点的数目？

解决此题：可以设置两个指针，一快一慢。

1.两个指针一个fast、一个slow同时从一个链表的头部出发
  fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇，（如果相遇就证明此链表包含环，否则没有环，解决问题1）

2.1 此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
    这次两个指针一次走一步，相遇的地方就是入口节点（解决问题2，得到环的入口节点）。

2. 2  接着步骤1，如果两个指针相遇，必然在环内，所以可以从这个节点出发，一遍继续向前移动，一遍计数，
当再次回到这个节点时，就可以得到环中节点数了（解决问题3，得到环中节点数目）
'''
def entryNodeOfLoop(pHead):
    pFast = pHead
    pSlow = pHead

    if pFast == None or pFast.next == None:
        return None

    while pFast != None and pSlow != None:
        pFast = pFast.next.next 
        pSlow = pSlow.next 

        # 两指针相遇且非空，则说明有环
        if pFast == pSlow:
            break   
        
        else:
            pFast = pFast.next 
            pSlow = pSlow.next
    # pFast = pHead
    # while pFast != pSlow:
    #     pFast = pFast.next 
    #     pSlow = pSlow.next

    return pFast # 返回入口节点

#-------------求解环中节点个数-----------------------
def EntryNodeOfLoop(pHead):
    pFast = pHead
    pSlow = pHead

    if pFast == None or pFast.next == None:
        return None

    while pFast != None and pSlow != None :
        pFast = pFast.next.next 
        pSlow = pSlow.next 

        # 两指针相遇且非空，则说明有环
        if pFast == pSlow:
            break

    meetingNode = pFast
    nodeInLoop = 1
    while pFast.next != meetingNode:
        pFast = pFast.next 
        nodeInLoop += 1

    return nodeInLoop  # 返回环中节点数目