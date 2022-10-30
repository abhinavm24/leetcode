#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.66%)
# Likes:    3072
# Dislikes: 4360
# Total Accepted:    340.8K
# Total Submissions: 672.6K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
# 
# 
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
# 
# 
# Constraints:
# 
# 
# -1000 <= a, b <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:

        # # log(2^a * 2^b)
        # return int(math.log2(2**a * 2**b))


        # 1, 1
        # def add(a, b):
        #     if not a or not b:
        #         return a or b
        #     return add(a ^ b, (a & b) << 1)

        # if a * b < 0:  # assume a < 0, b > 0
        #     if a > 0:
        #         return self.getSum(b, a)
        #     if add(~a, 1) == b:  # -a == b
        #         return 0
        #     if add(~a, 1) < b:  # -a < b
        #         return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        # return add(a, b)  # a*b >= 0 or (-a) > b > 0


        # # 1, 1
        # # 32 bit mask in hexadecimal, limit to 32 bits in python
        # mask = 0xffffffff
        
        # # works both as while loop and single value check 
        # while (b & mask) > 0:
            
        #     carry = ( a & b ) << 1
        #     a = (a ^ b) 
        #     b = carry
        
        # # handles overflow
        # return (a & mask) if b > 0 else a

        # recursion
        # https://leetcode.com/problems/sum-of-two-integers/discuss/963706/Python-or-Recursive-solution-or-Thought-Process
        mask = 0b11111111111111111111111111111111       
        MAX =  0b01111111111111111111111111111111
        
        if b == 0:
            return a if a <= MAX else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )



        # '''
        #     Problem: We want to add 2 numbers without using the + or -
        #              operators.
            
        #     Solution: We can use bit-wise manipulation but
        #              we need to write down all the possible cases:
        #                 a: +  b: +  
        #                 a: -  b: -
        #                 a: +  b: - 
        #                 b: -  b: +
                    
        #             For all problems:
        #                 1. We automatically do all our calculations with abs(a) and abs(b)
        #                     a, b = abs(a), abs(b)
        #                 2. We always ensure that abs(a) < abs(b), otherwise we switch a/b
                        
        #             SubProblem - 1: a + b
        #                 We can use the algorithm in I, where we contiously update sumNoCarry and carry
        #                 until carry = 0.
                        
        #                  while carry = 0      
        #                     sumNoCarry = a & b            =   a + b (w/o carry)
        #                     carry = (a ^ b) << 1          =   carry       
        #                     a, b = sumNoCarry, carry      =   a + b + carry
                
                            
        #             SubProblem-2: -a + (-b)
        #                 We can use the algorithm in I, where we contiously update sumNoCarry and carry
        #                 until carry = 0. Because python keeps track of negative indices
                    
        #             SubProblem-3 & SubProblem-4: a - b  OR  b - a
        #                 If we have subtraction, we use borrow instead, where we use NOT to invert the given number
        #                 while borrow = 0
        #                     sumNoBorrow = a & b         = a - b (w/o carry)
        #                     borrow = (~a * b) << 1      = borrow
        #                     a, b, = sumNoBorrow, borrow = a - b + borrow
            
        #     Time: O(1) because each integer contains 32 bits.
        #     Space: O(1) because we don't use any additional data structures.
                        
        #     WhiteBoard:
        #         I: a * b > 0    [+a,+b] OR [-a, -b]
                
        #             --- iteration 1 ---
        #             a = 15          01111 
        #             b = 2           00010   
        #             a + b = 17      10001       [SOLUTION]
        #             a ^ b           01101        = sum w/o carry (a)
        #             a & b           00010        
        #             (a&b) << 1      00100        = carry (b)


        #             Solution = (a^b) + ((a&b) << 1) = (01101 + 00100) = 10101
        #                 The sub-problem is the same as the problem, so we can use a loop
        #                 The base-case would be when our carry = 0

        #             --- iteration 2 ---
        #             a =  x & y           01101   = 13   
        #             b = (x&y) << 1       00100   = 4

        #             x = 13      01101
        #             y = 4       00100
        #             x^y         01001       = sum w/o carry(a)
        #             x&y         00100
        #             (x^y)<<1    01000       = carry (b)
                
                    
        #             --- iteration 3 ---
        #             a =  x & y           01001   = 9  
        #             b = (x&y) << 1       01000   = 8

        #             x = 9       01001
        #             y = 8       01000
        #             x^y         00001       = sum w/o carry(a)
        #             x&y         01000
        #             (x^y)<<1    10000       = carry (b)
                    
        #               --- iteration 3 ---
        #             a =  x & y           00001   = 1
        #             b = (x&y) << 1       10000   = 16
                    
        #             x = 16      00001
        #             y = 4       10000
        #             x^y         10001       = sum w/o carry(a)
        #             (x^y)<<1    00000       = carry (b)
                    
        #             carry = 0, so we return 10001 = 10101 = 17
                 
        #         II: a * b < 0    [-a,+b] OR [a, -b]
        #             --- iteration 1 ---
        #             a = -16      1..10000   MSB = flag for +/-
        #             b = 15          01111 
        #             a + b = 13   1..00001       [SOLUTION]
        #             a = abs(a)      10000
        #             a ^ b           11111   =  31 <-------------- SUM W/O CARRY ---
        #             ~a =         1..10001   = -17
        #                =         0..01110     <-- 1. Flipped
        #                =         0..01111     <-- 2. Add 1
        #             (~a&b)       0..01111   =  15  
        #             (~a&b)<<1       11110   = 15 * 2^2 = 30   <---- CARRY ----
                    
        #              --- iteration 2 ---
        #             a =  a ^ b           011111   = 31 
        #             b = (~a&b) << 1      011110   = 30
        #             a ^ b                000001   = 1
        #             ~a                0..100000   = -32
        #                               1..011111   <-- Flip
        #                               1..100000   <-- Add 1
        #             (~a & b)                0
                    
        #                 return -1
                    
                                    
        #         0b10001
        #         0b01111
        #           1111

        #             Solution = (a^b) + ((a&b) << 1) = (01101 + 00100) = 10101
        #                 The sub-problem is the same as the problem, so we can use a loop
        #                 The base-case would be when our carry = 0


                
            
        # '''
        # # 0. Get the absolutes values of both numbers
        # absA, absB = abs(a), abs(b)
        
        # # 1. Ensure that abs(a) >= abs(b)
        # if absA < absB:
        #     return self.getSum(b, a)
        
        # # 2. Store the sign - it will negative if the greater number if negative (a will always be greater)
        # sign = -1 if a < 0 else 1
                
        # # 3. Perform bit-wise operations to compute the sum
        # # 3a. If both a & b have the same sign [+a, +b] OR [-a, -b]
        # if a * b >= 0:
        #     # Continue looping until the amount to carry (b) is 0
        #     while absB:
        #         # Calculate the sum without carry using XOR
        #         sumWithoutCarry = absA ^ absB
        #         # Calculate the amount to carry using AND and a left-wise shift
        #         carry = (absA & absB) << 1
        #         # We are now left with a sub-problem where sum = sumWithoutCarry + carry
        #         absA, absB = sumWithoutCarry, carry
        
        # # 3b. a & b have different signs [-a, +b] OR [+a, -b]
        # else:
        #     # Continue looping until the amount to borrow (b) is 0
        #     while absB:
        #         # Calculate the sum w/o borrow using XOR
        #         sumWithoutBorrow = absA ^ absB
        #         # Calculate the amount to borrow using NOT, AND and a left-wise shift
        #         borrow = (~absA & absB) << 1
        #         # We are now left with a sub-problem where sum = sumWithoutBorrow + borrow
        #         absA, absB = sumWithoutBorrow, borrow
        
        # # 4. Return the solution
        # return sign * absA
        
# @lc code=end

