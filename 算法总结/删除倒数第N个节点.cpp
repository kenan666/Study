/*
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。


示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.


 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        ListNode * dummyHead = ListNode(0);
        dummyHead->next = head;

        ListNode * p = dummyHead;
        ListNode * q = dummyHead;

        for (int i = 0; i < n+1; i++)
        {
            q = q-> next;
        }
        while(q)
        {
            p = p-> next;
            q = q-> next;
        }
        ListNode * delNode = p->next;
        p->next = delNode->next;
        delete delNode;

        ListNode * retNode = dummyHead->next;
        delete dummyHead;

        return retNode;
    }
};

// 解2
/*
一趟扫描，
求解删除倒数第i个节点，等于找到链表中第（n-i+1）节点的位置，并将此删除
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        int count = 0;  // 存放链表长度
        ListNode * p = head;
        while(p)
        {
            //计算链表长度
            count ++;
            p = p->next;
        }
        p = head;

        if (count == 1) //链表只有一个元素
            return {};

        else if (count - n == 0)  //删除的是第一个元素
            return head->next;

        else
        {
            for (int i = 1;i<count-n;i++)
            {
                p = p->next;
            }
            p->next = p->next->next;
        }
        return head;
    }
};

