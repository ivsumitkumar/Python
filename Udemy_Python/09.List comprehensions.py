list0 = [letter for letter in range(1, 20)]
print("List0:", list0)

list1 = [letter * 2 for letter in range(1, 20) if letter % 2 == 0]
print("List1:", list1)

list2 = ['even' if letter % 2 == 0 else 'odd' for letter in range(1, 20)]
print("List2:", list2)

list3 = [x * y for x in range(3) for y in range(3)]
print("List3:", list3)

list4 = [[x for x in range(3)] for y in range(4)]
print("List4:", list4)
