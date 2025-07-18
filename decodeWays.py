
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if s[0] == "0":
        return 0
    elif len(s) == 1:
        return

    t = [0 for _ in range(len(s))]
    t[0] = 1

    if s[1] == "0":
        t[1] = 1
    else:
        t[1] = 2
    for i in range(2, len(s)):
        if s[i] != "0" and s[i - 1] != "0":
            if int(s[i] + s[i - 1]) <= 26:
                t[i] = t[i - 1] + t[i - 2]
            else:
                t[i] = t[i - 1]
        elif s[i] == "0":
            t[i] = t[i - 2]
        elif s[i - 1] == 0:
            t[i] = t[i - 1]
    return t[-1]


print(numDecodings("226"))
