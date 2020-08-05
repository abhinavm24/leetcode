#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """[summary]
        Maintain dictionary/hash map of complementary values of seen nums
        Check for num availability in dictionary to avoid two passes
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
            else:
                seen[target - num] = i
        return []


# @lc code=end
