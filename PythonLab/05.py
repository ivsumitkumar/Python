def sqroot(n, li):
    x = n
    count = 0
    while (1):
        print("x is", x)
        count += 1
        root = 0.5 * (x + (n / x))
        print("root might be: ", root)
        if (abs(root - x) < 1):
            break
        x = root
        return root


n = 327
li = 0.00001
print(sqroot(n, 1))
