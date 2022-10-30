# @before-stub-for-debug-begin
from collections import defaultdict
from turtle import left, right
from python3problem424 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (51.36%)
# Likes:    6437
# Dislikes: 254
# Total Accepted:    348.1K
# Total Submissions: 677.8K
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        freq = defaultdict(int) # defaultdict(int) returns 0 by default, even for nonexistent keys
        
        for right in range(len(s)):
            freq[s[right]] += 1
            currLen = right - left + 1
            if (currLen - max(freq.values())) > k:
                freq[s[left]] -= 1
                left += 1
            else:
                maxLen = max(maxLen, currLen)
        return maxLen

        # l = 0
        # freq = {}
        # maxlen = 0
        # for r in range(len(s)):
        #     # If a character is not in the frequency dict, this inserts it with a value of 1 (get returns 0, then we add 1).
        #     # If a character is in the dict, we simply add one.
        #     freq[s[r]] = freq.get(s[r], 0) + 1
                
        #     # The key point is that we only care about the MAXIMUM of the seen values.
        #     # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
        #     cur_len = r - l + 1
        #     if cur_len - max(freq.values()) <= k:  # if we have replaced <= K letters, record a new maxLen
        #         maxlen = max(maxlen, cur_len)
        #     else:                               # if we have replaced > K letters, then it's time to slide the window
        #         freq[s[l]] -= 1                 # decrement frequency of char at left pointer, then increment pointer
        #         l += 1
        # return maxlen

        
# @lc code=end

