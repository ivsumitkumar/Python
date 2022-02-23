'''
Level:>>> Medium
Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.

Example 1:

Input:
N = 10
Linked List = 30->23->28->30->11->14->
              19->16->21->25 
Output : 11 14 16 19 21 23 25 28 30 30 
Explanation :
The resultant linked list is sorted.
Example 2:

Input : 
N = 7
Linked List=19->20->16->24->12->29->30 
Output : 12 16 19 20 24 29 30 
Explanation : 
The resultant linked list is sorted.
Your task:
You don't need to read input or print anything. Your task is to complete the function insertionSort() which takes the head of the linked list, sorts the list using insertion sort algorithm and returns the head of the sorted linked list.
 
Expected Time Complexity : O(n2)
Expected Auxiliary Space : O(1)
 
Constraints:
1<=n<=10^5

RELATED TOPICS:>>>
Linked List

SAMPLE INPUT:>>>
1
10
30 23 28 30 11 14 19 16 21 25 
OUTPUT:>>>
11 14 16 19 21 23 25 28 30 30
'''
#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,x):
        var=Node(x)
        var.next=self.head
        self.head=var
class Solution:
    def insertionSort(self, head):
        #code here
        l=[]
        while head:
            l.append(head.data)
            head=head.next
        l.sort()
        l=l[::-1]
        li=LinkedList()
        for i in l:
            li.insert(i)
        return li.head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
INF = float("inf")
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = Node(INF)
        nodes = list(map(int, input().strip().split()))
        ptr = a
        for x in nodes:
            ptr.next = Node(INF)
            ptr = ptr.next
            ptr.data = x
        a = a.next
        ob=Solution()
        head = ob.insertionSort(a)
        printList(head)
# } Driver Code Ends