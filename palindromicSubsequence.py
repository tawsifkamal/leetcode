"""
Palindromic Subsequence Generation Algorithm

This module generates all possible palindromic subsequences from a given string
using dynamic programming approach.

Algorithm: Dynamic programming with substring expansion
Time Complexity: O(n^3) where n is length of string
Space Complexity: O(n^2)

Author: Leetcode Practice
"""

def solution(s):
    # find palindromic substrings!!
    indexToPalindromes = {}

    for i in range(len(s)):
        indexToPalindromes[i] = [s[i]]
        for j in range(i):
            if s[j] == s[i]:
                indexToPalindromes[i].append(s[j] + s[i])
                for x in range(j + 1, i):
                    for q in range(len(indexToPalindromes[x])):
                      indexToPalindromes[i].append(
                         s[j] + indexToPalindromes[x][q] + s[i])

    print(indexToPalindromes)


solution("attract")
