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
