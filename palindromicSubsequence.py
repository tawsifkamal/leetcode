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
