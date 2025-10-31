
def solution(s):
    """
    Decodes a string that follows a specific encoding rule.

    The encoding rule is: k[encoded_string], where the encoded_string
    inside the square brackets is being repeated exactly k times.

    Args:
      s: The encoded string.

    Returns:
      The decoded string.
    """
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
