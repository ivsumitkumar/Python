from random import shuffle, randint

list = [1, 2, 3, 4, 5]
shuffle(list)
print(list)
# shuffle is not allowed in tuple


num = randint(0, 200)
print(num)

a = input("Number")
print(type(a))
# input always returns str type
