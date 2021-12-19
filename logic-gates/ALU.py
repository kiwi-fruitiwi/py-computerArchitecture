from adders import half_adder, full_adder


def ALU(a, b, c, opcode):
    if opcode == 0:
        return half_adder(a, b)
    if opcode == 1:
        return full_adder(a, b, c)