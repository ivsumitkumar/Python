'''
LEVEL:>>> Medium

Given a binary tree and a node, print all cousins of given node in order of their appearance. Note that siblings should not be printed.

Example 1:

Input : 
             1
           /   \
          2     3
        /   \  /  \
       4    5  6   7

Given node : 5
Output : 6 7
Explanation :
Nodes 6 and 7 are on the same level 
as 5 and have different parents.

Example 2 :

Input :
         9
        /
       5
Given node : 5
Output : -1
Explanation :
There no other nodes than 5 in the same level.
Your task :
You don't have to read input or print anything. Your task is to complete the function printCousins() which takes the root node of the tree and the node whose cousins need to be found, as input and returns a list containing the cousins of the given node in order of their appearance in the tree. If there is no cousin of the given node, return -1 as the first element of the list.
 
Expected Time Complexity : O(n)
Expected Auxiliary Space : O(n)
 
Constraints :
1 <= n <=10^5

Related Topics:>>> Tree

SAMPLE INPUT:>>>
1
5
1 2 3 4 5 6 7
OUTPUT:>>> 6 7

SAMPLE INPUT:>>>
1
5
6 5
OUTPUT:>>> -1

'''
#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
                
    def printCousins(self, root, node_to_find):
        if root == node_to_find:
            return [-1]
            
        q = deque([root])
        parents = {}
        temp = None
        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    parents[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    parents[curr.right] = curr
                    q.append(curr.right)
                    
            if node_to_find in q:
                temp = [x for x in q]
                break
            
        res = []
        for node in temp :
                if parents[node]!= parents[node_to_find]:
                    res.append(node.data)
        return res if res else [-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
    
def pointer(root, n):
    if root == None:
        return None
    
    if root.data == n:
        return root
        
    l= pointer(root.left, n)
    if l != None and l.data==n :
        return l
    
    r= pointer(root.right, n)
    return r
    
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n=int(input())
        s=input()
        root = buildTree(s)
        p = pointer(root, n)
        ob = Solution()
        ans = ob.printCousins(root, p)
        
        for i in range(len(ans)):
           print(ans[i], end=" ")
                
        print()
            
# } Driver Code Ends