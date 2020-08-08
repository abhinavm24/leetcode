#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.40%)
# Likes:    2728
# Dislikes: 1905
# Total Accepted:    781.9K
# Total Submissions: 2.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """[summary]

        Args:
            strs (List[str]): [description]

        Returns:
            str: [description]
        """
        if not strs:
            return ""

        return reduce(self.get_common_prefix, strs)

# divide and conquer by reduce
    def get_common_prefix(self, x, y):
        LCP_length = 0

        for i in range(0, min(len(x), len(y))):
            if x[i] != y[i]:
                break

            LCP_length += 1

        return x[:LCP_length]

    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return ""

    #     minLen = len(strs[0])
    #     for i in range(len(strs)):
    #         minLen = min(len(strs[i]), minLen)

    #     lcp = ""
    #     i = 0
    #     while i < minLen:
    #         char = strs[0][i]
    #         for j in range(1, len(strs)):
    #             if strs[j][i] != char:
    #                 return lcp
    #         lcp = lcp + char
    #         i += 1

    #     return lcp


# @lc code=end
