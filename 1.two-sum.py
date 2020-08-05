#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.59%)
# Likes:    16018
# Dislikes: 581
# Total Accepted:    3.1M
# Total Submissions: 6.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """[summary]
        Maintain a dictionary with complementary num as key and index as value
        Check if number available in dict, to avoid two runs over list
        Return empty list if no solution

        Args:
            nums (List[int]): [description]
            target (int): [description]

        Returns:
            List[int]: [description]
        """

        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [seen[num], i]
            seen[target - num] = i
        return []

# @lc code=end
