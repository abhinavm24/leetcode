# @before-stub-for-debug-begin
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.75%)
# Likes:    29362
# Dislikes: 1249
# Total Accepted:    3.9M
# Total Submissions: 11.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # brute force for each possible substring
        # def check(start, end):
        #     chars = set()
        #     for i in range(start, end + 1):
        #         c = s[i]
        #         if c in chars:
        #             return False
        #         chars.add(c)
        #     return True

        # maxLen = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if check(i, j):
        #             res = max(maxLen, j - i + 1)
        # return maxLen



        # cache the position of each char in current sub str
        seen = {}
        # position of the longest and start char in current sub str
        maxLength = start = 0
        for index, alphabet in enumerate(s):
            # if alphabet is seen and int the current subtstring
            if alphabet in seen and start <= seen[alphabet]:
                # update to new start position of substring, ie. alphbet next to duplicate since, it's not repalced already
                start = seen[alphabet] + 1
            else:
                # if not seen update the max length
                maxLength = max(maxLength, index - start + 1)
            # update the cache with new alphabet
            seen[alphabet] = index

        return maxLength

        
# @lc code=end

