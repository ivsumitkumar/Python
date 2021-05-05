def binary(n):
    if n >= 1:
        return bin(n).replace("0b", "")
    else:
        return 0


n = int(input("Decimal value: "))
n = binary(n)
print("Binary: ", n)
