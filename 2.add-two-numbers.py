#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (39.64%)
# Likes:    22030
# Dislikes: 4296
# Total Accepted:    3.2M
# Total Submissions: 8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry = 0
        # head = curr = ListNode(-1)
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     carry, val = divmod(carry, 10)
        #     curr.next = curr = ListNode(val)
        # return head.next
        a=str(l1.val); b= str(l2.val)
        next= l1.next
        while next:
          a=str(next.val)+a
          next= next.next
        next= l2.next
        while next:
          b= str(next.val)+b
          next= next.next
          
        c= str(int(a)+int(b))
        i= len(c)-1
        l3= ListNode(int(c[i]))
        next= l3
        while i:          
          i-=1
          ch= int(c[i])
          if next != None:
            next.next= ListNode(ch)          
            next= next.next
        return l3


        
# @lc code=end

