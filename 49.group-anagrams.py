#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (65.84%)
# Likes:    12047
# Dislikes: 373
# Total Accepted:    1.6M
# Total Submissions: 2.5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashMap = defaultdict(list)
        # for str in strs:
        #     key = [0] * 26
        #     for chr in str:
        #         key[ord(chr) - ord("a")] += 1
        #     hashMap[tuple(key)].append(str)
        # return hashMap.values()

        
        # nlog(max size of string), 
        # hashMap = defaultdict(list)
        # for str in strs:
        #     sortedStr = "".join(sorted(str))
        #     hashMap[sortedStr].append(str)
        # return hashMap.values()

        
# @lc code=end
