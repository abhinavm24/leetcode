#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.72%)
# Likes:    16281
# Dislikes: 824
# Total Accepted:    2.8M
# Total Submissions: 6.8M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False


        # # The stack to keep track of opening brackets.
        # stack = []

        # # Hash map for keeping track of mappings. This keeps the code very clean.
        # # Also makes adding more types of parenthesis easier
        # mapping = {")": "(", "}": "{", "]": "["}

        # # For every bracket in the expression.
        # for char in s:

        #     # If the character is an closing bracket
        #     if char in mapping:

        #         # Pop the topmost element from the stack, if it is non empty
        #         # Otherwise assign a dummy value of '#' to the top_element variable
        #         top_element = stack.pop() if stack else '#'

        #         # The mapping for the opening bracket in our hash and the top
        #         # element of the stack don't match, return False
        #         if mapping[char] != top_element:
        #             return False
        #     else:
        #         # We have an opening bracket, simply push it onto the stack.
        #         stack.append(char)

        # # In the end, if the stack is empty, then we have a valid expression.
        # # The stack won't be empty for cases like ((()
        # return not stack



        # # if else written with continue and a delayed pop
        # Map = {")": "(", "]": "[", "}": "{"}
        # stack = []

        # for c in s:
        #     if c not in Map:
        #         stack.append(c)
        #     else:
        #         if not stack or stack[-1] != Map[c]:
        #             return False
        #         stack.pop()

        # return not stack   
        # 
        # 
        # # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0   

        
# @lc code=end

