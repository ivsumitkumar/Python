a = 'Subscribe '
print(a)
b = len(a)
print("Length of a:", b)

c = a.upper()
print('Upper case of a:', c)

d = a.lower()
print("Lower of a:", d)

e = a.swapcase()
print("a after swapping case:", e)

f = a.isalpha()
print("Only alphabets in a:", f)

g = a.isalnum()
print("Only alphabets and numbers in a:", g)

h = a.isdigit()
print("Only Digits in a:", h)

i = a.replace("Sub", "di")
print("Replaced 'Sub' with 'di' in a:", i)

j = a.index(' ')
print("Index of ' '(white space) in a:", j)

k = a.strip()  # to remove whitespaces from left use>> a.lstrip()
# to remove whitespaces from right use>> a.rstrip()
print("No white spaces in a:", k)

L = a.split('b')
print("list of a:", L)

m = list([1, 2.5, 3, "YO", 7])
print(m[0:4:2], m[3], m[1])
