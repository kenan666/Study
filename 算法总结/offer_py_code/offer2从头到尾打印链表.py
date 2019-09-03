'''
题目：从尾到头打印链表

输入一个链表，从尾到头打印链表每个节点的值。
'''
# 解1  -->使用栈,可以使用列表模拟
def printLinks(links):
    stack = []

    while links:
        stack.append(links.val)
        links = links.next

    while stack:
        print (stack.pop())

# 解 2  --> 递归
def printLinkrecursion(links):
    if links :
        printLinkrecursion(links.next)
        print (links.val)

# 解3  --> # 返回从尾部到头部的列表值序列，
def printListFromTailToHead(listNode):
    if not listNode:
        return False

    res = []
    while listNode.next is not None:
        res.append(listNode.val)
        listNode = listNode.next

    res.append(listNode.val)
    return res[::-1]