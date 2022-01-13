a = [1, 'apple', 3, 4.0, 'Mango', 5, 'Yeah']

print('List is: ',a)

a.append('dog')
print('List after append is: ', a)

a.insert(2, 'Tasty')
print('List after insert is: ', a)

a.pop()  # it returns the deleted element as value
print('List after pop is: ', a)

a.remove('Tasty')
print('List after remove is: ', a)

del a[1:3]
print('List after del is: ', a)

a.reverse()
print('List after reverse is: ', a)

b = [5, 7, 6, 2, 1, 5, 3, 4]
print(b)
b.sort()  # It doesn't work on heterogeneous list.
print('List after sort is: ', b)
