#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.73%)
# Likes:    4591
# Dislikes: 148
# Total Accepted:    729.4K
# Total Submissions: 1.5M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start


from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        """[summary]

        Args:
            n (int): [description]

        Returns:
            int: [description]
        """

        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return b


# Improved

def climbStairs1(self, n):
    if n < 4:
        return n
    else:
        a, b = 3, 5
        for i in range(5, n+1):
            a, b = b, a+b
        return b

# Top down - TLE


def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1) + self.climbStairs(n-2)


# Top down - TLE with memoization


@lru_cache(maxsize=45)
def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1) + self.climbStairs(n-2)

# Bottom up, O(n) space


def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]

# Bottom up, constant space


def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b

# Top down + memorization (list)


def climbStairs4(self, n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return self.helper(n-1, dic)


def helper(self, n, dic):
    if dic[n] < 0:
        dic[n] = self.helper(n-1, dic) + self.helper(n-2, dic)
    return dic[n]

# Top down + memorization (dictionary)


def __init__(self):
    self.dic = {1: 1, 2: 2}


def climbStairs(self, n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dic[n]


# Top down + memorization (dictionary) simple


def climbStairs(self, n, dic={}):
    if n < 4:
        return n
    if n not in dic:
        dic[n] = self.climbStairs(n-1, dic) + self.climbStairs(n-2, dic)
    return dic[n]

# @lc code=end
