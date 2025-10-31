def solution(p, v):
    """
    This function finds if an anagram of p is a substring of v.

    Args:
      p: The pattern string.
      v: The text string to search in.

    Returns:
      True if an anagram of p is a substring of v, False otherwise.
    """
    l = 0

    dictV = {}
    dictP = {}
    vs = set()

    for i in range(len(p)):
        dictP[p[i]] = dictP.get(p[i], 0) + 1
        dictV[p[i]] = 0

    for r in range(len(v)):
        # This while loop is to shrink the window from the left
        while v[r] in dictP and dictP[v[r]] == dictV[v[r]]:
            dictV[v[l]] -= 1
            l = l + 1

        if v[r] in dictP:
            dictV[v[r]] = dictV.get(v[r], 0) + 1
            vs.add(v[r])

            if r - l + 1 == len(p):
                return True
        elif v[r] not in dictP:
            # Reset the window and the dictionary
            while len(vs) != 0:
                letter = vs.pop()
                dictV[letter] = 0

            l = r + 1

    return False


res = solution("abcdd", "dmabaddddvsdvdssdvsdvcdddbcg")
print(res)


def solution2(v, p):
    """
    This function finds if an anagram of p is a substring of v using a sliding window approach.

    Args:
      v: The text string to search in.
      p: The pattern string.

    Returns:
      True if an anagram of p is a substring of v, False otherwise.
    """
    if len(v) < len(p):
        return False

    l = 0
    r = 0

    dictP = {}
    dictV = {}

    for i in range(len(p)):
        dictP[p[i]] = dictP.get(p[i], 0) + 1

    # Initialize the first window
    while r < len(p):
        if v[r] in dictP:
            dictV[v[r]] = dictV.get(v[r], 0) + 1

        r = r + 1

    while r < len(v) - 1:
        if dictV == dictP:
            return True

        # Slide the window
        if v[l] in dictP:
            dictV[v[l]] -= 1

        r += 1
        l += 1

        if v[r] in dictP:
            dictV[v[r]] = dictV.get(v[r], 0) + 1

    if dictV == dictP:
        return True

    return False


res2 = solution2("dmabacddg", "abcdd")

print(res2)
