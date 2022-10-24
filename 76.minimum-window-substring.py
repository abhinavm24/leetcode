#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (39.97%)
# Likes:    12591
# Dislikes: 579
# Total Accepted:    877.5K
# Total Submissions: 2.2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #         def allFound(s):
#             sCounter = Counter([ele for ele in s if ele in t])
#             return all([tCounter[ele] <= sCounter[ele] for ele in tCounter])


#         tCounter = Counter(t)
#         minLength = sys.maxsize
#         result = ""
#         for left in range(len(s)):
#             for right in range(1, len(s)+1):
#                 if allFound(s[left:right]):
#                     if minLength > len(s[left:right]):
#                         result = s[left:right]
#                         minLength = len(s[left:right])
#         return result
        
        
#         if t == "":
#             return ""

#         countT, window = {}, {}
#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)

#         have, need = 0, len(countT)
#         res, resLen = [-1, -1], float("infinity")
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1

#             while have == need:
#                 # update our result
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = r - l + 1
#                 # pop from the left of our window
#                 window[s[l]] -= 1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1
#         l, r = res
#         return s[l : r + 1] if resLen != float("infinity") else ""




#         # Struggled with this problem for a long while.
#         # Idea: Two pointers: moving end forward to find a valid window,
#         #                     moving start forward to find a smaller window
#         #                     counter and hash_map to determine if the window is valid or not

#         # Count the frequencies for chars in t
#         hash_map = dict()
#         for c in t:
#             if c in hash_map:
#                 hash_map[c] += 1
#             else:
#                 hash_map[c] = 1

#         start, end = 0, 0

#         # If the minimal length doesn't change, it means there's no valid window
#         min_window_length = len(s) + 1

#         # Start point of the minimal window
#         min_window_start = 0

#         # Works as a counter of how many chars still need to be included in a window
#         num_of_chars_to_be_included = len(t)

#         while end < len(s):
#             # If the current char is desired
#             if s[end] in hash_map:
#                 # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
#                 if hash_map[s[end]] > 0:
#                     num_of_chars_to_be_included -= 1
#                 # And we decrease the hash_map value
#                 hash_map[s[end]] -= 1

#             # If the current window has all the desired chars
#             while num_of_chars_to_be_included == 0:
#                 # See if this window is smaller
#                 if end - start + 1 < min_window_length:
#                     min_window_length = end - start + 1
#                     min_window_start = start

#                 # if s[start] is desired, we need to update the hash_map value and the counter
#                 if s[start] in hash_map:
#                     hash_map[s[start]] += 1
#                     # Still, update the counter only if the current char is "critical"
#                     if hash_map[s[start]] > 0:
#                         num_of_chars_to_be_included += 1

#                 # Move start forward to find a smaller window
#                 start += 1

#             # Move end forward to find another valid window
#             end += 1

#         if min_window_length == len(s) + 1:
#             return ""
#         else:
#             return s[min_window_start:min_window_start + min_window_length]
    
    
    
            need = Counter(t)            #hash table to store char frequency
            missing = len(t)                         #total number of chars we care
            start, end = 0, 0
            i = 0
            for j, char in enumerate(s, 1):          #index j from 1
                if need[char] > 0:
                    missing -= 1
                need[char] -= 1
                if missing == 0:                     #match all chars
                    while i < j and need[s[i]] < 0:  #remove non useful chars
                        need[s[i]] += 1
                        i += 1
                    need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                    missing += 1                     #we will miss this first char, so add missing by 1
                    if end == 0 or j-i < end-start:  #update window
                        start, end = i, j
                    i += 1                           #update i to start+1 for next window
            return s[start:end]

        
# @lc code=end

