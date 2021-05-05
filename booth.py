def toBinary(dec, ch):  # decimal to binary
    global qSign
    global mSign
    if ch == 'q':
        qSign = 0 if(dec > 0) else 1
        print("Binary of", dec)
        temp = bin(dec)
        global Q
        Q = list(temp[qSign + 2::])  # slicing to remove 0b/-0b
    elif ch == 'm':
        mSign = 0 if(dec > 0) else 1
        print("Binary of", dec)
        temp = bin(dec)
        global M
        M = list(temp[mSign + 2::])  # slicing to remove 0b/-0b


def onesComp(ch):
    for i in range(len(ch)):
        ch[i] = 1 if int(ch[i]) == 0 else 0


def twosComp(ch):
    for i in range(len(ch) - 1, -1, -1):
        if ch[i] == 1:
            ch[i] = 0
        else:
            ch[i] = 1
            break


def bitChecker():
    while(len(Q) != len(M)):
        Q.insert(0, qSign) if(len(Q) < len(M)) else M.insert(
            0, mSign)  # equating the no. of bits


def generation(q, m):
    toBinary(q, 'q')  # Q generation starts
    if(q < 0):
        onesComp(Q)
        twosComp(Q)
        Q.insert(0, 1)
    print("Q==", *Q, sep='')
    toBinary(m, 'm')  # M generation starts
    if(m < 0):
        onesComp(M)
        twosComp(M)
        M.insert(0, 1)
    print("M==", *M, sep='')
    bitChecker()
    print("equating bits")
    print("Q==", *Q, sep='')
    print("M==", *M, sep='')
    global M1  # M1 generation starts
    M1 = list(M)
    m1Sign = 1 if(mSign == 0) else 0
    onesComp(M1)
    twosComp(M1)
    if m1Sign == 1:  # if M1 is negative
        M1.insert(0, m1Sign)
        Q.insert(0, qSign)
        M.insert(0, mSign)
    print("Final values are:")
    print("M1==", *M1, sep='')
    print("Q==", *Q, sep='')
    print("M==", *M, sep='')
    global A  # A generation starts
    A = [0] * len(Q)
    print("A==", *A, sep='')
    global count
    count = len(A)
    print("count=", count)
    global Q_  # creating Q-1
    Q_ = 0


def add():
    carry = 0
    for i in range(len(M) - 1, -1, -1):
        temp = (int(A[i]) + int(M[i]) + carry) % 2
        carry = (int(A[i]) + int(M[i]) + carry) // 2
        A[i] = temp


def sub():
    carry = 0
    for i in range(len(M1) - 1, -1, -1):
        temp = (A[i] + M1[i] + carry) % 2
        carry = (A[i] + M1[i] + carry) // 2
        A[i] = temp


def shift():
    global Q_
    Q_ = Q[len(Q) - 1]
    for i in range(len(Q) - 1, 0, -1):
        Q[i] = Q[i - 1]
    Q[0] = A[len(A) - 1]
    for i in range(len(A) - 1, 0, -1):
        A[i] = A[i - 1]


def printLine(step):
    print(count, end='\t\t')
    print(*A, sep='', end='\t')
    print(*Q, sep='', end='\t')
    print(Q_, "\t", step)


def algo():
    print("Starting algo.....")
    global count
    print("count\tA", count * ' ', "\tQ", count * ' ', "\tQ_\t step")
    printLine("initial")
    while (count > 0):
        if(int(Q[len(Q) - 1]) == 1 and int(Q_) == 0):
            sub()
            printLine("A<--A-M")
        elif (int(Q[len(Q) - 1]) == 0 and int(Q_) == 1):
            add()
            printLine("A<--A+M")
        count = count - 1
        shift()
        printLine("ASR A,Q,Q_ and count--")
    print("final product: ", *A, sep='', end='')
    print(*Q, sep='')


def main():
    generation(int(input("Enter Q: ")), int(input("Enter M: ")))
    algo()


if __name__ == "__main__":
    main()
