'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

import math


class Solution(object):
    def addDigits(self, num):
        return num - 9 * int(math.floor((num - 1) / 9)) if num != 0 else 0
