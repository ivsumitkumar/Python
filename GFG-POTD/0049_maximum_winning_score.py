'''
LEVEL:>>> Medium
In an online game, N blocks are arranged in a hierarchical manner. All the blocks are connected together by a total of N-1 connections. Each block is given an ID from 1 to N. A block may be further connected to other blocks. Each block is also assigned a specific point value.

A player starts from Block 1. She must move forward from each block to a directly connected block until she reaches the final block, which has no further connection. When the player lands on a block, she collects the point value of that block. The players score is calculated as the product of point values that the player collects.
Find the maximum score a player can achieve.
Note: The answer can always be represented with 64 bits.


Example 1:

Input:
     4
    / \
   2   8
  / \ / \
 2  1 3  4
Output: 128
Explanation: Path in the given tree 
goes like 4, 8, 4 which gives the max
score of 4x8x4 = 128.
Example 2:

Input:
     10
   /    \
  7      5
          \
           1
Output: 70
Explanation: The path 10, 7 gives a 
score of 70 which is the maximum possible.

Your Task:
You don't need to take input or print anything. Your task is to complete the function findMaxScore() that takes root as input and returns max score possible.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).


Constraints:
1 ≤ Number of nodes ≤ 103
1 ≤ Data on node ≤ 10
It is guaranteed that the answer will always fit in the 64-bit Integer

Related Topics:>>>
Binary Search Tree

SAMPLE INPUT:>>>
1
4 2 8 2 1 3 4
OUTPUT:>>> 128

SAMPLE INPUT:>>>
1
5 2 3 6 4 9 8 7 4 1
OUTPUT:>>> 420
'''
#User function Template for python3

#structure of class Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def findMaxScore(self, root):
        #code here
        popv=[]
        product=1
        
        def recursion(root,product):
            product = product*root.data
            if root.left==None and root.right==None:
                popv.append(product)
            if root.left:
                recursion(root.left,product)
            if root.right:
                recursion(root.right,product)
        recursion(root,product)
        return max(popv)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob= Solution()
        
        print(ob.findMaxScore(root))

# } Driver Code Ends