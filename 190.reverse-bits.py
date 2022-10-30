# @before-stub-for-debug-begin
from python3problem190 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (51.81%)
# Likes:    3727
# Dislikes: 937
# Total Accepted:    546.6K
# Total Submissions: 1.1M
# Testcase Example:  '00000010100101000001111010011100'
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# Note:
# 
# 
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 2 above, the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.
# 
# 
# 
# Example 1:
# 
# 
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100
# represents the unsigned integer 43261596, so return 964176192 which its
# binary representation is 00111001011110000010100101000000.
# 
# 
# Example 2:
# 
# 
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101
# represents the unsigned integer 4294967293, so return 3221225471 which its
# binary representation is 10111111111111111111111111111111.
# 
# 
# 
# Constraints:
# 
# 
# The input must be a binary string of length 32
# 
# 
# 
# Follow up: If this function is called many times, how would you optimize it?
# 
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:

        # # internal
        # # get 32 bit binary rep and reverse and back to int
        # return int('{:032b}'.format(n)[::-1], base=2)

        # # 1, 1
        res = 0
        for i in range(32):
            if ((n >> i) & 1):
                res += 1 << (31-i)
        return res
        
# @lc code=end

