'''
Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.
Example 1:

Input:
5 3
1 2 3 4 5

Output: 
3 2 1 4 5

Explanation:
After reversing the given
input from the 3rd position the resultant
output will be 3 2 1 4 5.
'''

def modifyQueue(q, k):
    # code here
    l1 = q[0:k]
    del q[0:k]
    l1.reverse()
    return l1 + q

n = int(input("Enter Length of Queue: "))
ke = int(input("Enter number of element to be reversed:"))
qu = [x for x in range(1, n+1)]

print('\nQueue is:',qu)
print(f'Reverse of first {ke} elements is: {modifyQueue(qu,ke)}')