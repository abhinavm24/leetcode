# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.83%)
# Likes:    11400
# Dislikes: 423
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
from collections import Counter, defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        # if k == len(nums):
        #     return nums


        # map=Counter(nums)
        # return sorted(map, key=map.get, reverse=True)[:k]


        # # Counter and most common, slow..
        # return [k for k,v in Counter(nums).most_common(k)]
        

        # # counter and max heap
        # most_common is implement using nlargest anyway, it takes nlogk everything else is linear
        # nlogk, n+k
        # map = Counter(nums)
        # return heapq.nlargest(k, map, key=map.get)


        # counter and loop for top 2
        # frequency = defaultdict(list)
        # bigger = 0
        # for num, count in Counter(nums).items():
        #     frequency[count].append(num)
        #     bigger = max(bigger, count)
        
        # result = []
        # for times in range(bigger, 0, -1):
        #     result.extend(frequency[times] if k - len(result) >= len(frequency[times]) else frequency[:k - len(result)])
        #     if len(result) == k:
        #         break

        # return result

        # n, n
        # count and bucket sort
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count:
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
# @lc code=end

