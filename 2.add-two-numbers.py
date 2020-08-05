#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.84%)
# Likes:    8687
# Dislikes: 2193
# Total Accepted:    1.5M
# Total Submissions: 4.3M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """[summary]
        Loop through two linked lists
            accumulate carry
            update pointer
        Create new node with remainder
        Update carry with modulus
        Update pointer

        Args:
            l1 (ListNode): [description]
            l2 (ListNode): [description]

        Returns:
            ListNode: [description]
        """

        dummyNode = ptr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            ptr.next = ListNode(carry % 10)
            ptr = ptr.next
            carry //= 10
        return dummyNode.next

        # addends = l1, l2
        # dummy = end = ListNode(0)
        # carry = 0
        # while addends or carry:
        #     carry += sum(a.val for a in addends)
        #     addends = [a.next for a in addends if a.next]
        #     end.next = end = ListNode(carry % 10)
        #     carry //= 10
        # return dummy.next

        # left = 0
        # dummy = cur = ListNode(-1)
        # while l1 or l2 or left:
        #     left, sm = divmod(sum(l and l.val or 0 for l in (l1, l2)) + left, 10)
        #     cur.next = cur = ListNode(sm)
        #     l1 = l1 and l1.next
        #     l2 = l2 and l2.next
        # return dummy.next

        # @lc code=end
