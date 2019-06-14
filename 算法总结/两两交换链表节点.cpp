/*
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例：
给定 1->2->3->4, 你应该返回 2->1->4->3.

 */
/*
关键思路

递归

关注点：
1、返回值：交换完成的子链表
2、调用单元：设需要交换的两个点为 head 和 next，head 连接后面交换完成的子链表，next 连接 head，完成交换
3、终止条件：head 为空指针或者 next 为空指针，也就是当前无节点或者只有一个节点，无法进行交换


 */
class Solution 
{
    public ListNode swapPairs(ListNode head) 
    {
        if(head == null || head.next == null)
        {
            return head;
        }
        ListNode next = head.next;
        head.next = swapPairs(next.next);
        next.next = head;
        return next;
    }
}


//  非递归
class Solution
{
    public ListNode swapPairs(ListNode head)
    {
        ListNode pre = new ListNode(0);
        pre.next = head;
        ListNode temp = pre;
        while(temp. next != null && temp.next.next != null)
        {
            ListNode start = temp.next;
            ListNode end = temp.next.next;
            temp.next = end.next;
            start.next = end;
            end.next = start;
            temp = start;
        }
        return pre.next;
    }
}