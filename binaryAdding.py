def getSum(a, b):
    """
    This function adds two integers by converting them to binary strings and
    performing addition bit by bit.

    Args:
      a: The first integer.
      b: The second integer.

    Returns:
      The sum of the two integers.
    """
    binaryA = bin(a)[2:]
    binaryB = bin(b)[2:]

    # Pad the shorter binary string with zeros
    maxLength = max(len(binaryA), len(binaryB))
    binaryA = binaryA.zfill(maxLength)
    binaryB = binaryB.zfill(maxLength)

    sumBinary = ""
    isCarry = 0

    # Iterate from right to left
    for i in range(maxLength - 1, -1, -1):
        bitA = int(binaryA[i])
        bitB = int(binaryB[i])

        # Calculate the sum of bits and carry
        bitSum = bitA + bitB + isCarry

        sumBinary = str(bitSum % 2) + sumBinary
        isCarry = bitSum // 2

    if isCarry:
        sumBinary = "1" + sumBinary

    return int(sumBinary, 2)

print(getSum(1, 2))