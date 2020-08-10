#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (46.50%)
# Likes:    8369
# Dislikes: 397
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Tracking running sum if prev sum is non-zero
        else start new array sum

        Args:
            nums (List[int]): [description]

        Returns:
            int: [description]
        """
        maxSum = float("-inf")
        runningSum = 0
        for num in nums:
            if runningSum > 0:
                runningSum += num
            else:
                runningSum = num
            maxSum = max(maxSum, runningSum)
        return maxSum


# @lc code=end
