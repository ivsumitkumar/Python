'''
LEVEL:>>> Easy
Given a linked list, the task is to move all 0s to the front of the linked list. The order of all another element except 0 should be same after rearrangement.

Example 1:

Input:  0 -> 4 -> 0 -> 5 -> 0
Output: 0 -> 0 -> 0 -> 4 -> 5
Explanation: After moving all 0s of the given
list to the front, the list is:
0 -> 0 -> 0 -> 4 -> 5
Example 2:

Input: 0 -> 1 -> 0 -> 1 -> 2
Output: 0 -> 0 -> 1 -> 1 -> 2
Your Task:
You don't need to read input or print anything. Your task is to complete the function moveZeroes() which takes head node of the linked list as input parameter.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 50

Related Topics:>>>
Linked List

SAMPLE INPUT:>>>
1
20
5 0 6 6 2 2 8 10 8 4 8 8 8 1 1 5 0 4 6 4

OUTPUT:>>>
0 0 4 6 4 5 1 1 8 8 8 4 8 10 8 2 2 6 6 5 
'''
#User function Template for python3

# Linked List Node Structure

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None  '''
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
  
    def push(self, val):
  
    # 1 & 2: Allocate the Node & 
    #        Put in the data 
        new_node = Node(val) 
          
    # 3. Make next of new Node as head 
        new_node.next = self.head 
          
    # 4. Move the head to point to new Node  
        self.head = new_node 
    
    def moveZeroes(self):
        temp=self.head
        prev=None
        count=0
        while(temp):
            if(temp.data==0 and prev!=None ):
                count+=1
                prev.next=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        while(count):
            self.push(0)
            count-=1
        return self.head
        
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        lis = LinkedList()
        n = int(input())
        arr = list(map(int, input().strip().split()))
        #head = createList(arr, n)
        for i in range(0,len(arr)):
            lis.push(arr[i])
        lis.moveZeroes()
        lis.display()
        print()
# } Driver Code Ends