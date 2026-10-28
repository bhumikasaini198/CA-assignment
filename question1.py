
def to_binary(n):
    return format(n & 0xFF, '08b')

def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value

def binary_arithmetic(a, b, operation):
    bin_a = to_binary(a)
    bin_b = to_binary(b)

    if operation == '+':
        result = a + b
    else:
        result = a - b

    bin_result = to_binary(result)
    overflow = result < -128 or result > 127

    print("First operand :", bin_a, "(", a, ")")
    print("Second operand:", bin_b, "(", b, ")")
    print("Operation     :", operation)
    print("Result (8-bit):", bin_result)
    print("Decimal result:", signed_value(bin_result))
    print("Overflow      :", "Yes" if overflow else "No")
    print()

print("a) +46 + (+29)")
binary_arithmetic(46, 29, '+')

print("b) (-48) - (-23)")
binary_arithmetic(-48, -23, '-')
