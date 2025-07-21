"""
Word Break Dynamic Programming Algorithm

This module determines if a string can be segmented into space-separated 
sequence of dictionary words using dynamic programming.

Algorithm: Bottom-up dynamic programming
Time Complexity: O(n^2 * m) where n is string length, m is dictionary size
Space Complexity: O(n)

Author: Leetcode Practice
"""

def wordBreak(s, wordDict):
    t = [False for _ in range(len(s) + 1)]
    t[-1] = True

    for starting in range(len(s) - 1, -1, -1):
        for ending in range(starting, len(s)):
            for word in wordDict:
                if s[starting: ending + 1] == word:
                    t[starting] = t[starting + len(word)]
    print(t)
    return t[0]


wordBreak("leetcode", ["leet", "code"])
