DEBUG = True


# adds two bits! provides a carry bit and sum bit as a tuple
def half_adder(a, b):
    s = a ^ b
    c = a & b
    return s, c


# display for half_adder
if DEBUG:
    # test cases for HALF_ADDER
    print("\nTest cases for half adder")
    print("A: 0, B: 0 | Output: {0}".format(half_adder(0, 0)))
    print("A: 0, B: 1 | Output: {0}".format(half_adder(0, 1)))
    print("A: 1, B: 0 | Output: {0}".format(half_adder(1, 0)))
    print("A: 1, B: 1 | Output: {0}".format(half_adder(1, 1)))


# adds two bits and a carry bit, returning a sum and carry bit itself.
def full_adder(a, b, c):
    # the sum bit, s, is the sum of a, b, c. we use two half_adders
    s_intermediate, c_1 = half_adder(a, b)
    s, c_2 = half_adder(c, s_intermediate)
    c_out = c_1 | c_2
    return s, c_out


if DEBUG:
    # test cases for FULL_ADDER
    print("\nTest cases for full adder")
    print("A: 0, B: 0, C: 0 | Output: {0}".format(full_adder(0, 0, 0)))
    print("A: 0, B: 0, C: 1 | Output: {0}".format(full_adder(0, 0, 1)))
    print("A: 0, B: 1, C: 0 | Output: {0}".format(full_adder(0, 1, 0)))
    print("A: 0, B: 1, C: 1 | Output: {0}".format(full_adder(0, 1, 1)))
    print("A: 1, B: 0, C: 0 | Output: {0}".format(full_adder(1, 0, 0)))
    print("A: 1, B: 0, C: 1 | Output: {0}".format(full_adder(1, 0, 1)))
    print("A: 1, B: 1, C: 0 | Output: {0}".format(full_adder(1, 1, 0)))
    print("A: 1, B: 1, C: 1 | Output: {0}".format(full_adder(1, 1, 1)))