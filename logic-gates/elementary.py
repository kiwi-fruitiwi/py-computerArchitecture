def NAND_gate(a, b):
    if a:
        if b:
            return 0
    return 1


# test cases for NAND
print("\nTest cases for NAND gate")
print("A: 0, B: 0 | Output: {0}".format(NAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(NAND_gate(1, 1)))


def NOT_gate(i):
    return NAND_gate(i, i)


# test cases for NOT
print("\nTest cases for NOT gate")
print("A: 0 | Output: {0}".format(NOT_gate(0)))
print("A: 1 | Output: {0}".format(NOT_gate(1)))


def AND_gate(a, b):
    return NOT_gate(NAND_gate(a, b))


# test cases for AND
print("\nTest cases for AND gate")
print("A: 0, B: 0 | Output: {0}".format(AND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(AND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(AND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(AND_gate(1, 1)))


def OR_gate(a, b):
    return NOT_gate(AND_gate(NOT_gate(a), NOT_gate(b)))


print("A: 0, B: 0 | Output: {0}".format(OR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(OR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(OR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(OR_gate(1, 1)))


def XOR_gate(a, b):
    return OR_gate(
        AND_gate(a, NOT_gate(b)),
        AND_gate(NOT_gate(a), b)
    )


# test cases for XOR
print("\nTest cases for OR gate")
print("A: 0, B: 0 | Output: {0}".format(XOR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(XOR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(XOR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(XOR_gate(1, 1)))