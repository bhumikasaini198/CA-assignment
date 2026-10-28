
def ror(binary, positions):
    print("\nRotate Right Without Carry (ROR)")
    print("Original:", binary)

    for i in range(positions):
        last_bit = binary[-1]
        binary = last_bit + binary[:-1]
        print("Step", i + 1, ":", binary)

    print("Final result:", binary)


def rcr(binary, carry, positions):
    print("\nRotate Right With Carry (RCR)")
    print("Original:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        last_bit = binary[-1]
        binary = str(carry) + binary[:-1]
        carry = int(last_bit)

        print("Step", i + 1, ":", binary,
              "Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)


number = "11010101"

ror(number, 3)
rcr(number, 0, 3)
