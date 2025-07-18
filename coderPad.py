

# # Given an encoded string, return its decoded string.

# # The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# # You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# # The test cases are generated so that the length of the output will never exceed 105.

# # Example 1:

# # Input: s = "3[a]2[bc]"
# # Output: "aaabcbc"

# # Example 2:



# # # Example 3:

# # # Input: s = "2[ab3[ac]]"
# # # Output: ""

# #  2(ab + acacac) = 2 * abacacac = abacacacabacacac

# # Input: s = "3[a]2[bc]"
# #                     i
# # prefix = '' => 'a' => aaa => '' => b => bc
# # k = '' => '3' => '' => 2 => ''
# # stack = []

# # '' + 3 * prefix => aaa + 2 * bc = aaabcbc


# # ######## Example TWo #####


# for i in s:
#    if s[i] a number:
#       k = k + s[i] 
#    if s[i] a alpha:
#       prefix = prefix + s[i]
#    if s[i] is "]":
#       pop of my stack
#       previousPrefix, wordMultiplier = stack.pop()

#       prefix = previousPrefix + wordMultiplier * prefix
#    if s[i] is "[":
#       push onto stack (prefix, k)
#       also reset k
#       also reset prefix



# # Input: s = "2[ab3[ac]]ef"
#                          i
# prefix = '' => 'a' => 'ab' => '' => 'a' => 'ac' => 'abacacac' => abacacacabacacac => abacacacabacacacef
# k = '' => 2 => '' => 3 => ''
# stack = []

# prefix = previousPrefix + k * prefix
# 1. prefix =  'ab' + 3 * ac = 'abacacac'
# 2. prefix = '' + 2 * 'abacacac' = 'abacacacabacacac


def solution(s):
    k = ''
    prefix = ''
    stack = []

    for i in range(len(s)):
        if s[i].isdigit():
            k += s[i]
        elif s[i].isalpha():
            prefix += s[i]
        elif s[i] == "[":
            stack.append((prefix, k))
            prefix = ''
            k = ''
        elif s[i] == "]":
            previousPrefix, multiplier = stack.pop()
            prefix = previousPrefix + int(multiplier) * prefix

    return prefix

res = solution("2[ab3[ac]]ef")
print(res)


