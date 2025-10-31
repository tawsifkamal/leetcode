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
    """
    This function finds if a permutation of pattern p exists in string v.

    Args:
      p: The pattern string.
      v: The string to search in.

    Returns:
      True if a permutation of p is found in v, False otherwise.
    """
    l = 0

    dictV = {}
    dictP = {}
    vs = set()

    # Create a frequency map of characters in the pattern p
    for i in range(len(p)):
        dictP[p[i]] = dictP.get(p[i], 0) + 1
        dictV[p[i]] = 0

    # Iterate through the string v with a sliding window
    for r in range(len(v)):
        # If the current character is in the pattern and its count in the current window (dictV)
        # is already equal to its count in the pattern (dictP), shrink the window from the left
        while v[r] in dictP and dictP[v[r]] == dictV[v[r]]:
            dictV[v[r]] -= 1
            l = l + 1

        if v[r] in dictP:
            # If the current character is in the pattern, increment its count in the window
            dictV[v[r]] += 1
            vs.add(v[r])

            # If the window size is equal to the pattern length, we found an anagram
            if r - l + 1 == len(p):
                return True
        elif v[r] not in dictP:
            # If the current character is not in the pattern, reset the window and the counts
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
    """
    This function finds if a permutation of pattern p exists in string v using a sliding window approach.

    Args:
      v: The string to search in.
      p: The pattern string.

    Returns:
      True if a permutation of p is found in v, False otherwise.
    """
    if len(v) < len(p):
        return False

    l = 0
    r = 0

    dictP = {}
    dictV = {}

    # Create a frequency map of characters in the pattern p
    for i in range(len(p)):
        dictP[p[i]] = dictP.get(p[i], 0) + 1

    # Initialize the sliding window and its character frequency map
    while r < len(p):
        if v[r] in dictP:
            dictV[v[r]] = dictV.get(v[r], 0) + 1
        r = r + 1

    # Slide the window across the string v
    while r < len(v):
        if dictV == dictP:
            return True

        if r < len(v):
            # Expand the window from the right
            if v[r] in dictP:
                dictV[v[r]] = dictV.get(v[r], 0) + 1
            r += 1

        # Shrink the window from the left
        if r - l > len(p):
            if v[l] in dictP:
                dictV[v[l]] -= 1
                if dictV[v[l]] == 0:
                    del dictV[v[l]]
            l += 1

    if dictV == dictP:
        return True

    return False


res2 = solution2("dmabacddg", "abcdd")

print(res2)
