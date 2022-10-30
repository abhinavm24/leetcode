#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (49.07%)
# Likes:    38759
# Dislikes: 1244
# Total Accepted:    8M
# Total Submissions: 16.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
# 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Brute Force
        # Time  complexity: O(n^2)
        # Space complexity: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 2. Two-pass Hash Table
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # hash_table = {}
        # for i, num in enumerate(nums):
        #     hash_table[num] = i
        # for i, num in enumerate(nums):
        #     j = hash_table.get(target - num)
        #     if j is not None and i != j:
        #         return [i, j]

        # 3. One-pass Hash Table
        # Time  complexity: O(n)
        # Space complexity: O(n)
        hash_table = {}
        for i, num in enumerate(nums):
            j = hash_table.get(target - num)
            if j is not None:
                return [j, i]
            hash_table[num] = i
        return []
        
        # More
        # https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
        
        
# @lc code=end

