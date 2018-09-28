"""
两数相加
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/82/

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(-1)                   # 头结点
        tmp = re
        # add = False                       # 不加add标志位，通过最后扫描一遍
        while l1 != None and l2 != None:
            v = l1.val+l2.val            
            tmp.next = ListNode(v)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2 != None:
            tmp.next = l2
        if l1 != None and l2 == None:
            tmp.next = l1
        
        # 检查进位
        tmp = re
        while tmp.next != None:
            if tmp.val >= 10:
                tmp.val = tmp.val-10
                tmp.next.val += 1
            tmp = tmp.next
        if tmp.val >= 10:
            tmp.val -= 10
            tmp.next = ListNode(1)
        return re.next
                
