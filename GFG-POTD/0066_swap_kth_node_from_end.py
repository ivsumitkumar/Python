''''
LEVEL:>>> Medium
Given a singly linked list of size N, and an integer K. You need to swap the Kth node from the beginning and Kth node from the end of the linked list. Swap the nodes through the links. Do not change the content of the nodes.

 

Example 1:

Input:
N = 4,  K = 1
value[] = {1,2,3,4}
Output: 1
Explanation: Here K = 1, hence after
swapping the 1st node from the beginning
and end thenew list will be 4 2 3 1.
 

Example 2:

Input:
N = 5,  K = 7
value[] = {1,2,3,4,5}
Output: 1
Explanation: K > N. Swapping is invalid. 
Return the head node as it is.
 

Your Task: 
You do not need to read input or print anything. The task is to complete the function swapkthnode(), which has takes head of link list, N and K as input parameters and returns the new head.
The generated output will be 1 if you are able to complete your task. 

 

Expected Time Complexity: O(n)
Expected Auxillary space Complexity: O(1)

 

Constraints:
1 <= N <= 103
1 <= K <= 103

Related Topic:>>>
Linked List

SAMPLE INPUT:>>>
1
4 1
1 2 3 4
OUTPUT:>>>
1
'''
#User function Template for python3
'''
Function Arguments :
        @param  : head (given head of linked list), k(value of k)
        @return : None, Just swap the nodes
        
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
from typing import *

def swapkthnode(head, num, k):
    if n<k:
        return head

    if (2 * k - 1) == n:
        return head

    x = head
    x_prev = Node(None)
    for i in range(k - 1):
        x_prev = x
        x = x.next

    
    y = head
    y_prev = Node(None)
    for i in range(n - k):
        y_prev = y
        y = y.next

    
    if x_prev is not None:
        x_prev.next = y

    if y_prev is not None:
        y_prev.next = x
     
   
    temp = x.next
    x.next = y.next
    y.next = temp

    if k == 1:
        head = y
     
    if k == n:
        head = x
    
    return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        new_head=swapkthnode(a.head,n, kth_node)

        new_check = [getNthfromEnd(new_head, kth_node), getNthfromBeg(new_head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)
# } Driver Code Ends