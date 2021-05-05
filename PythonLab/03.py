a = 20
b = 30
x = min(a, b)
for i in range(1, x):
    if(a % i == 0 and b % i == 0):
        gcd = i
print("Gcd is:", gcd)
