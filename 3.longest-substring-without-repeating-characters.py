# @before-stub-for-debug-begin
from python3problem3 import *
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
# Medium (30.37%)
# Likes:    9818
# Dislikes: 589
# Total Accepted:    1.6M
# Total Submissions: 5.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """[summary]

        Args:
            s (str): [description]

        Returns:
            int: [description]
        """

        # cache the position of each char in current sub str
        seen = {}
        # position of the longest and current and start char in current sub str
        maxLength = start = 0
        for index, alphabet in enumerate(s):
            # if alphabet is seen and int the current subtstring (otherwise start>current, another way to handle would be delete non current subtring alphabets)
            if alphabet in seen and start <= seen[alphabet]:
                # update to new start position of substring, ie. alphbet next to duplicate since, it's not repalced already
                start = seen[alphabet] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
            # update the cache with new substring
            seen[alphabet] = index

        return maxLength

# @lc code=end
