'''
LEVEL:>>> Medium
Given a graph with n vertices, e edges and an array arr[] denoting the edges connected to each other, check whether it is Biconnected or not.
Note: The given graph is Undirected.

 

Example 1:

Input:
n = 2, e = 1
arr = {0, 1}
Output:
1
Explanation:
       0
      /
     1
The above graph is Biconnected.
Example 2:

Input:
n = 3, e = 2
arr = {0, 1, 1, 2}
Output:
0
Explanation:
       0
      /
     1
      \
       2
The above graph is not Biconnected.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function biGraph() which takes 2 Integers n, and e and an array arr of length 2*e as input and returns 1 if the graph is biconnected else returns 0.

 
Expected Time Complexity: O(n+e)
Expected Auxiliary Space: O(n)

 
Constraints:
1 <= e <= 100
2 <= n <= 100

Related Topics:>>>
Graph

SAMPLE INPUT:>>>
1
2 1
0 1
OUTPUT:>>>
1
'''
#User function Template for python3

class Solution:
   def biGraph(self, arr, n, e):
       adj=[[] for _ in range(n)]
       for i in range(e):
           adj[arr[2*i]].append(arr[2*i+1])
           adj[arr[2*i+1]].append(arr[2*i])
       parent =[-1]*n
       visited=[True]+[False]*(n-1)
       depth=[0]+[-1]*(n-1)
       lowpoint=[0]+[-1]*(n-1)
       stack=[0]
       while stack:
           node=stack[-1]
           pop=True
           for i,node2 in enumerate(adj[node]):
               if node2!=parent[node] and not visited[node2]:
                   if node==0 and i>0:
                       return 0
                   visited[node2]=True
                   pop=False
                   stack.append(node2)
                   parent[node2]=node
                   depth[node2]=depth[node]+1
                   lowpoint[node2]=lowpoint[node]+1
                   break
           if pop:
               for node2 in adj[node]:
                   if parent[node2] == node and lowpoint[node2] >=depth[node] and len(stack)>=2:
                       return 0
                   if node2!=parent[node]:
                       lowpoint[node]=min(lowpoint[node],lowpoint[node2])
               stack.pop()
       for i in range(n):
           if not visited[i]:
               return 0
       return 1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.biGraph(arr,n,e))
# } Driver Code Ends