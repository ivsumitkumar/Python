# using built_in function
def binary(n):
    if n > 1:
        return bin(n).replace("0b", "")


num = int(input("Decimal value: "))
print("Binary:", binary(num))

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(m):

    if m > 1:
        DecimalToBinary(m // 2)
    print(m % 2, end='')

# Driver Code
# if __name__ == '__main__':


    # decimal value
dec_val = num

# Calling function
DecimalToBinary(dec_val)
