"""
Palindrome Validation Algorithm

This module checks if a string is a valid palindrome, ignoring non-alphanumeric
characters and case differences.

Algorithm: Two-pointer approach with character filtering
Time Complexity: O(n) where n is length of string
Space Complexity: O(1)

Author: Leetcode Practice
"""

def solution(s):
    if s == None or len(s) == 0:
        return False

    left = 0
    right = len(s) - 1
    cameAcrossLetter = False

    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            cameAcrossLetter = True
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        if not s[left].isalnum():
            left += 1
        if not s[right].isalnum():
            right -= 1

    if cameAcrossLetter == True:
        return True
    else:
        return False


res = solution(None)

print(res)
