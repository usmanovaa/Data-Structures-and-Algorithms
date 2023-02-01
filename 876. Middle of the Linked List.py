#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.

# Linked list, Two Pointers
# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# UPDATED, time complexity - O(logn)
# Runtime 19 ms Beats 68.95%, Memory 13.5 MB Beats 59.15%

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow



################################################

# INITIAL, time complexity - O(2n)
# Runtime 22 ms Beats 52.86% Memory 13.7 MB Beats 9.36%

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1

        if n // 2 == 0:
            n = n / 2
        else:
            n = n / 2 + 1        

        temp = head
        while n > 1:
            temp = temp.next
            n -= 1

        head = temp

        return head
