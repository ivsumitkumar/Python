'''
LEVEL:>>> Medium
Given a connected acyclic graph with n nodes and n-1 edges, count the pair of nodes that are at even distance(number of edges) from each other.


Example 1:

Input:
n = 3
graph = {{}, {2}, {1, 3}, {2}}
Output: 1
Explaination: Here there are three pairs {1,2},{1,3}
and {2,3} and only {1,3} has even distance between them.
i.e           1
             /
            2
           /
          3

Example 2:

Input:
n = 5
graph = {{}, {2,4}, {1,3}, {2}, {1,5}, {4}}
Output: 4
Explaination: There are four pairs {1,3},{1,5},{2,4}
and {3,5} which has even distance.

Your Task:
You don't need to read input or print anything. Your task is to complete the function countOfNodes() which takes the array graph[] (given as Adjacency list) and its size n as input parameters and returns the count of pair of nodes that are at even distance from each other


Expected Time Complexity: O(V+E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ n ≤ 104

Related Topics:>>>
Graph

SAMPLE INPUT:>>>
1
3
1 2 2 3
OUTPUT:>>>
1
'''
#User function Template for python3

class Solution:
   def countOfNodes(self, graph,n):
       # code here
       even=1
       odd=0
       q=[]
       q.append(1)
       flag=True
       visited={1}
       while q:
           p=[]
           while q:
               poped=q.pop(0)
               for i in graph[poped]:
                   if i not in visited:
                       p.append(i)
                       visited.add(i)
           if flag:
               odd+=len(p)
               flag=False
           else:
               even+=len(p)
               flag=True
           q=p
       return ((even)*(even-1)//2)+((odd)*(odd-1)//2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = input().split()
        graph = defaultdict(list)
        for i in range(0,2*n-2,2):
            graph[int(arr[i])].append(int(arr[i+1]))
            graph[int(arr[i+1])].append(int(arr[i]))
            
            
        
        ob = Solution()
        print(ob.countOfNodes(graph,n))
# } Driver Code Ends