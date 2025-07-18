
def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    binaryA = str(bin(a))[2:]
    binaryB = str(bin(b))[2:]
    
    aPointer = len(binaryA) - 1
    bPointer = len(binaryB) - 1
    sumBinary = ""
    isCarry = False
    print(binaryA)
    print(binaryB)
    while aPointer >= 0 and bPointer >= 0:
        if binaryA[aPointer] == "1" and binaryB[bPointer] == "1" and isCarry == True:
            sumBinary = "1" + sumBinary
            isCarry = True
        elif binaryA[aPointer] == "1" and binaryB[bPointer] == "1" and isCarry == False:
            sumBinary = "0" + sumBinary
            isCarry = True 
        elif ((binaryA[aPointer] == "1" and binaryB[bPointer] == "0") or (binaryA[aPointer] == "0" and binaryB[bPointer] == "1")) and isCarry == True:
            sumBinary = "0" + sumBinary
            isCarry = True
        elif ((binaryA[aPointer] == "1" and binaryB[bPointer] == "0") or (binaryA[aPointer] == "0" and binaryB[bPointer] == "1")) and isCarry == False:
            sumBinary = "1" + sumBinary
            isCarry = False
        elif binaryA[aPointer] == "0" and binaryB[bPointer] == "0" and isCarry == True:
            sumBinary = "1" + sumBinary
            isCarry = False
        elif binaryA[aPointer] == "0" and binaryB[bPointer] == "0" and isCarry == False:
            sumBinary = "0" + sumBinary
            isCarry = False
        aPointer -= 1
        bPointer -= 1
    while aPointer >= 0:
        if binaryA[aPointer] == "1" and isCarry == True:
            sumBinary = "0" + sumBinary
            isCarry = True
        elif binaryA[aPointer] == "1" and isCarry == False:
            sumBinary = "0" + sumBinary
            isCarry = False
        elif binaryA[aPointer] == "0" and isCarry == True:
            sumBinary = "1" + sumBinary
            isCarry = False
        elif binaryA[aPointer] == "1" and isCarry == True:
            sumBinary = "0" + sumBinary
            isCarry = False
        aPointer -= 1
    while bPointer >= 0:
        if binaryB[bPointer] == "1" and isCarry == True:
            sumBinary = "0" + sumBinary
            isCarry = True
        elif binaryB[bPointer] == "1" and isCarry == False:
            sumBinary = "0" + sumBinary
            isCarry = False
        elif binaryB[bPointer] == "0" and isCarry == True:
            sumBinary = "1" + sumBinary
            isCarry = False
        elif binaryB[bPointer] == "1" and isCarry == True:
            sumBinary = "0" + sumBinary
            isCarry = False
        bPointer -= 1
    if isCarry == True:
        sumBinary = "1" + sumBinary
    return int(sumBinary, 2)
    
print(getSum(1, 2))      