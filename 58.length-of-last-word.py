#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.56%)
# Likes:    686
# Dislikes: 2499
# Total Accepted:    386.2K
# Total Submissions: 1.2M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space
# characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#
#
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = ""
        for i in s[::-1].strip():
            if i != " ":
                result += i
            else:
                break
        return len(result)

    # fast internal functions
    def lengthOfLastWord(self, s: str) -> int:
        try:
            # get last word by splitting whitesoace and pick the first word in reversed direction
            last_word = next(reversed(s.split()))
            return len(last_word)

        except StopIteration:
            # if last word is empty, then directly return 0
            return 0

# @lc code=end
