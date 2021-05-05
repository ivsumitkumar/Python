def myf(name):
    print("Hello",name)

myf('Sumit')

def func(a,b):
    return a+b
result= func(23,52)
print(result)

def check_prime(num):
    flag=0
    for i in range(2,num):
        if (num%i==0):
            flag=1
            break
    return flag==0

result = check_prime(int(input("Enter Number")))
print(result)