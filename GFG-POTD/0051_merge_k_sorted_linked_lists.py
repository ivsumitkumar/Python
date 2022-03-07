'''
LEVEL:>>> Medium
Given K sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list.

Example 1:

Input:
K = 4
value = {{1,2,3},{4 5},{5 6},{7,8}}
Output: 1 2 3 4 5 5 6 7 8
Explanation:
The test case has 4 sorted linked 
list of size 3, 2, 2, 2
1st    list     1 -> 2-> 3
2nd   list      4->5
3rd    list      5->6
4th    list      7->8
The merged list will be
1->2->3->4->5->5->6->7->8.
Example 2:

Input:
K = 3
value = {{1,3},{4,5,6},{8}}
Output: 1 3 4 5 6 8
Explanation:
The test case has 3 sorted linked
list of size 2, 3, 1.
1st list 1 -> 3
2nd list 4 -> 5 -> 6
3rd list 8
The merged list will be
1->3->4->5->6->8.
Your Task:
The task is to complete the function mergeKList() which merges the K given lists into a sorted one. The printing is done automatically by the driver code.

Expected Time Complexity: O(nk Logk)
Expected Auxiliary Space: O(k)
Note: n is the maximum size of all the k link list

Constraints
1 <= K <= 103

Related Topics:>>>
Heap
Linked List

SAMPLE INPUT:>>>
1
4
3 1 2 3 2 4 5 2 5 6 2 7 8
OUTPUT:>>>
1 2 3 4 5 5 6 7 8 
'''
#User function Template for python3
'''
    Your task is to merge the given k sorted
    linked lists into one list and return
    the the new formed linked list class.

    Function Arguments:
        arr is a list containing the n linkedlist head pointers
        n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
class Solution:
   #Function to merge K sorted linked list.
   def mergeKLists(self,arr,K):
       # code here
       # return head of merged list
       l=[]
       for i in arr:
           temp=i
           while temp:
               l.append(temp.data)
               temp=temp.next
       l.sort()
       head=Node(l[0])
       str=head
       for i in range(1,len(l)):
           node=Node(l[i])
           str.next=node
           str=node
       return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends