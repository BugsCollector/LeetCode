"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        ret = []
        cur = self
        while cur:
            ret.append(cur.val)
            cur = cur.next
        print(ret)


class Solution(object):
    def translate(self, l):
        ret_head = ListNode('NaN')
        cur = ret_head
        for val in l:
            node = ListNode(val)
            if cur.val == 'NaN':
                cur = node
                ret_head = cur
            else:
                cur.next = node
                cur = cur.next
        return ret_head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_head = ListNode('NaN')
        cur = ret_head
        inc = 0
        while l1 or l2 or inc > 0:
            val = inc
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            inc = int(val / 10)
            node = ListNode(val % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if cur.val == 'NaN':
                cur = node
                ret_head = cur
            else:
                cur.next = node
                cur = cur.next

        return ret_head


obj = Solution()
l1 = [5]
l2 = [6]
l1_head = obj.translate(l1)
l2_head = obj.translate(l2)
ret = obj.addTwoNumbers(l1_head, l2_head)
ret.print()
