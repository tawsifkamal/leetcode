"""
Anagram Detection Algorithm Implementation

This module implements two different approaches to detect if any anagram of pattern 'p' 
exists as a substring in string 'v' using sliding window technique.

Algorithms implemented:
1. solution() - First approach using sliding window with character frequency tracking
2. solution2() - Second approach with optimized sliding window

Time Complexity: O(n) where n is length of string v
Space Complexity: O(k) where k is number of unique characters in pattern p

Author: Leetcode Practice
"""

import collections

'''
v = "dmabacddg"   r - l + 1 = len(p)
        l
            r
p = "abcdd" 

Letters of P
a -> 1
b -> 1
c -> 1
d -> 2

Letter of V
a -> 1
b -> 1
c -> 1
d -> 2

 012345678

v = "aaaaaabbaaaaaaaa"
p = "baaaaaaaa" 8a
"dmbaddacbg"
     l
         r

         O(n * m) where n is len(v) and m is len(p)
l = 0

LetterToIndex:
  (a, b, d)

for r in range(v):
  if r - l + 1 == len(p):
    return true
  while v[r] is in dictP and dictP.get(v[r]) == dictV.get(v[r]):
    dictV[v[l]] -= 1
    l = l + 1

  if v[r] is in dictP:
    dictV[v[r]] = dictV[v[r]] + 1


    add to dictionary with index as well (v[r])
  elif v[r] is not in dictP:
    while len(vs) != 0:
      letter, index = vs.pop()
      dictV[letter] = 0
    l = r + 1

return false
'''


def solution(p, v):
    l = 0

    dictV = {}
    dictP = {}
    vs = set()

    for i in range(len(p)):
        dictP[p[i]] = dictP.get(p[i], 0) + 1
        dictV[p[i]] = 0

    for r in range(len(v)):
        while v[r] in dictP and dictP[v[r]] == dictV[v[r]]:
            dictV[v[r]] -= 1
            l = l + 1

        if v[r] in dictP:
            dictV[v[r]] += 1
            vs.add(v[r])

            if r - l + 1 == len(p):
                return True
        elif v[r] not in dictP:
            while len(vs) != 0:
                letter = vs.pop()
                dictV[letter] = 0

            l = r + 1

    return False


res = solution("abcdd", "dmabaddddvsdvdssdvsdvcdddbcg")
print(res)


'''

        


lettersInP
a -> 1
b -> 1
c -> 1
d -> 2

lettersInV
a -> 0
b -> 0
c -> 0
d -> 1

v = "dmabacddg"
     l
         r  
          
p = "abcdd" 

if len(v) < len(p):
  return False

l = 0
r = len(p) - 1

while r < len(v) - 1: 
  r +=1
  l +=1

  take out letter in V at index L
  if v[l] in lettersInP:
    lettersInV[v[l]] -= 1

  take in letter in V at index R
  if v[r] in lettersInP:
    lettersInV[v[r]] += 1

  if twoHashMaps are equal:
    return True O(26 * n)
'''


def solution2(v, p):
    if len(v) < len(p):
        return False

    l = 0
    r = 0

    dictP = {}
    dictV = {}

    for i in range(len(p)):
        dictP[p[i]] = dictP.get(p[i], 0) + 1

    while r < len(p):
        if v[r] in dictP:
            dictV[v[r]] = dictV.get(v[r], 0) + 1
        r = r + 1

    
    while r < len(v) - 1:
        if dictV == dictP:
            return True

        if v[l] in dictP and v[l] in dictV:
            dictV[v[l]] -= 1

        r += 1
        l += 1

        if r < len(v) and v[r] in dictP:
            dictV[v[r]] += 1

    if dictV == dictP:
        return True

    return False


res2 = solution2("dmabacddg", "abcdd")

print(res2)
