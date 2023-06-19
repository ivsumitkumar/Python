list1 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15,44]
print('len of list1',len(list1))
print(list(filter(lambda x: x % 2 == 0, list1)))

##don,t use lambda in while creating large projects