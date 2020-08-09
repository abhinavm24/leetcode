#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (34.46%)
# Likes:    1663
# Dislikes: 1961
# Total Accepted:    691.3K
# Total Submissions: 2M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#
# Constraints:
#
#
# haystack and needle consist only of lowercase English characters.
#
#
#

# @lc code=start
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     """[summary]
    #
    #     Args:
    #         haystack (str): [description]
    #         needle (str): [description]
    #
    #     Returns:
    #         int: [description]
    #     """
    #
    #     return haystack.find(needle)

    # def strStr(self, haystack: str, needle: str) -> int:
    #     for index, alpha in enumerate(haystack):
    #         if alpha == needle[0]:
    #             if haystack[index:index+len(needle)] == needle:
    #                 return index
    #     return -1

    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle == '':
            return 0

        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i: i+n] == needle:
                return i

        return -1

# @lc code=end
