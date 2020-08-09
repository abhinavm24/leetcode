#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (53.44%)
# Likes:    4545
# Dislikes: 607
# Total Accepted:    1M
# Total Submissions: 2M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new sorted list. The new
# list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
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
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     dummy = cur = ListNode(0)
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next

    # recursively
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """[summary]

        Args:
            l1 (ListNode): [description]
            l2 (ListNode): [description]

        Returns:
            ListNode: [description]
        """

        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # in-place, iteratively
    # def mergeTwoLists(self, l1, l2):
    #     if None in (l1, l2):
    #         return l1 or l2
    #     dummy = cur = ListNode(0)
    #     dummy.next = l1
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             l1 = l1.next
    #         else:
    #             nxt = cur.next
    #             cur.next = l2
    #             tmp = l2.next
    #             l2.next = nxt
    #             l2 = tmp
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next

# @lc code=end
