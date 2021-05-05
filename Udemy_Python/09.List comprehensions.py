list = [letter for letter in range(1, 20)]
print(list)

list1 = [letter * 2 for letter in range(1, 20) if letter % 2 == 0]
print(list1)

list2 = ['even' if letter % 2 == 0 else 'odd' for letter in range(1, 20)]
print(list2)

list3 = [x * y for x in range(3) for y in range(3)]
print(list3)

list4 = [[x for x in range(3)] for y in range(4)]
print(list4)
