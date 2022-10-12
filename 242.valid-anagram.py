#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (62.67%)
# Likes:    7194
# Dislikes: 240
# Total Accepted:    1.7M
# Total Submissions: 2.8M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        # s+t, s+t
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]], countT[t[i]] = 1 + countS.get(s[i], 0), 1 + countT.get(t[i], 0)
        # return countS == countT


        # return Counter(s) == Counter(t)

        # s+t, s
        # tList = list(t)
        # for alphabet in s:
        #     if alphabet in tList:
        #         tList.remove(alphabet)
        #     else:
        #         return False
        # return len(tList)==0
        

        # Your runtime beats 73.5 % of python3 submissions
        # Your memory usage beats 96.8 % of python3 submissions (14.5 MB)
        # return all(s.count(x)==t.count(x) for x in set(s+t))


        # Your runtime beats 99.46 % of python3 submissions
        # Your memory usage beats 34.99 % of python3 submissions (14.6 MB)
        # return not any(s.count(x)!=t.count(x) for x in set(s+t))


        # nlogn, 1
        # return sorted(s) == sorted(t)
        
# @lc code=end

