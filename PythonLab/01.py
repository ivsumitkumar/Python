import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nName of Python script:", sys.argv[0])
print("\nArguments passed:")
for i in range(1, n):
    print(sys.argv[i])
Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])
print("\n\nResult:", Sum)
