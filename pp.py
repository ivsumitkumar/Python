# n= int(input("Enter THe number:"))
# if n>1:
# 	for i in range(2,n):
# 		if n%i==0:
# 			print(n,"is Not Prime Number.")
# 			break
# 	else:
# 		print(n,"is a Prime Number.")
# else:
# 	print(n,"is not a prime number.")


'''******************************************************'''
'''To Print The prime no. in a given range'''

# lwr = int(input("Enter the Lower no.:"))
# upr = int(input("Enter the upper no.:"))
# print("Prime Numbers Between", lwr, "and", upr, "is:")
# if lwr == 0:
#     lwr = lwr + 2
# elif lwr == 1:
#     lwr = lwr + 1

# for i in range(lwr, upr + 1):
#     if i > 1:
#         for x in range(2, i):
#             if i % x == 0:
#                 break

#         else:
#             print(i)

'''*****************************************************'''
'''Fibonacci Series'''

# n=int(input("Enter the upper limit:"))
# a,b=0,1
# print(a)
# print(b)
# c=a+b
# print(c)
# while c<n:
# 	a=b
# 	b=c
# 	c=a+b
# 	if c<n:
# 		print(c)

'''*****************************************************'''
'''To check if the given no. is a Fibonacci no. or not'''

# import math

# def perfectsquare(x):
# 	s= int(math.sqrt(x))
# 	if x==s*s:
# 		return 1
# 	else:
# 		return 0
# n=int(input("Enter any Number:"))
# if (perfectsquare(5*(n*n)+4)==1 or perfectsquare(5*(n*n)-4)==1):
# 	print(n,'is a Fibonnaci number.')
# else :
# 	print(n,'is not a Fibonnaci number.')

'''*****************************************************'''
'''Armstorng Number in a given interval'''

# l=int(input("Enter Range\nFrom: "))
# u=int(input("To: "))
# if l<=0:
# 	l=1
# for i in range(l,u+1):
# 	p=len(str(i))
# 	s=0
# 	t=i

# 	while t>0:
# 		d=t%10
# 		s+=d**p
# 		t//=10
# 	if s==i:
# 		print(i)

'''*****************************************************'''
'''Program to find the sum of square of first n natural numbers'''

# n= int(input("Enter The Number:"))
# sum=0
# for i in range(1,n+1):
# 	sum=sum+(i*i)

# print("Sum of natural numbers till",n,"is",sum)

'''*****************************************************'''
# Python program to convert decimal into other number systems
# dec = int(input("Enter The Number:"))

# print("The decimal value of", dec, "is:")
# print(bin(dec).replace("0b",""), "in binary.")
# print(oct(dec).replace("0o",""), "in octal.")
# print(hex(dec).replace("0x",""), "in hexadecimal.")

'''*****************************************************'''
# Program to find the ASCII value of the given character

# c = input("Enter any character:")
# print("The ASCII value of '" + c + "' is", ord(c))

'''*****************************************************'''
# to print greater number

# a= int(input('Enter 1st number:'))
# b= int(input('Enter 2nd number:'))
# c= int(input('Enter 3rd number:'))
# if a>b:
# 	if b>c:
# 		print(a,'is greater.')
# elif b>a:
# 	if a>c:
# 		print(b,'is greater.')
# elif c>a:
# 	if a>b:
# 		print(c,'is greater.')
# else:
# 	print('Same Numbers.')

'''*****************************************************'''
# to reverse a string

# n= input('Enter a string:\n')
# print(n[::-1])

'''*****************************************************'''
# Python 3 program to find factorial of given number
# def factorial(n):
# 	return 1 if (n==1 or n==0) else n * factorial(n - 1)

# num=int(input("Enter the number: "))
# print ("Factorial of",num,"is",factorial(num))

'''*****************************************************'''
# Python program to find the L.C.M. of two input number

# This function computes GCD
# def compute_gcd(x, y):
#    while(y):
#        x, y = y, x % y
#        print('x=',x,'y=',y)
#    return x
# # This function computes LCM
# def compute_lcm(x, y):
#    lcm = (x*y)//compute_gcd(x,y)
#    print(lcm,'lcm')
#    return lcm
# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# print("The L.C.M. is", compute_lcm(num1, num2))

'''*****************************************************'''
# Python program of Tower of Hanoi

# print((1,2,3) + (4,5,6))
# print(("hi",)*3)
# n = int(input('enter the number of disks:'))

# def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
#     if n == 1:
#         print("Move disk1th 1 from rod", from_rod, "To rod", to_rod)
#         return
#     TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
#     print("Movedisk2th", n, "from rod", from_rod, "to rod", to_rod)
#     TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

# TowerOfHanoi(n, 'A', 'C', 'B')

# i=5
# while True:
# 	if i%0011 == 0:
# 		break
# 	print(i)

# 	i+=1
