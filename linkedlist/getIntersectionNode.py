"""
相交链表
编写一个程序，找到两个单链表相交的起始节点。

 

例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
在节点 c1 开始相交。

 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
 

致谢:
特别感谢 @stellari 添加此问题并创建所有测试用例。
"""

"""
https://blog.csdn.net/jiqiren007/article/details/6572685
"""


# Definition for singly-linked list.
# class ListNode():
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    
    def traverse(self, l):
        if l == None:
            retrun (0,None)
        num = 1
        while l.next != None:
            num += 1
            l = l.next
        return (num,l)
    
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        lenA, lastA = self.traverse(headA)
        lenB, lastB = self.traverse(headB)
        length = 0
        if lastA != lastB:
            return None
        if lenA >= lenB:
            longOne = headA
            shortOne = headB
            length = lenA - lenB
        if lenA < lenB:
            longOne = headB
            shortOne = headA
            length = lenB - lenA
            
        for i in range(length):
            longOne = longOne.next
        while longOne != None:
            if longOne == shortOne:
                return longOne
            longOne = longOne.next
            shortOne = shortOne.next
        
            
    
