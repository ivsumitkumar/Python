'''
LEVEL<:>>> Medium
Given a weighted directed graph with n nodes and m edges. Nodes are labeled from 0 to n-1, the task is to check if it contains a negative weight cycle or not.
Note: edges[i] is defined as u, v and weight.
 

Example 1:

Input: n = 3, edges = {{0,1,-1},{1,2,-2},
{2,0,-3}}
Output: 1
Explanation: The graph contains negative weight
cycle as 0->1->2->0 with weight -1,-2,-3.
Example 2:

Input: n = 3, edges = {{0,1,-1},{1,2,-2},
{2,0,3}}
Output: 0
Explanation: The graph does not contain any
negative weight cycle.
 

Your Task:
You don't need to read or print anyhting. Your task is to complete the function isNegativeWeightCycle() which takes n and edges as input paramater and returns 1 if graph contains negative weight cycle otherwise returns 0.
 

Expected Time Complexity: O(n*m)
Expected Space Compelxity: O(n)
 

Constraints:
1 <= n <= 100
1 <= m <= n*(n-1), where m is the total number of Edges in the directed graph.

Related Topics:>>>
Graph

SAMPLE INPUT:>>>
1
3 3
0 1 -1
1 2 -2
2 0 -3

OUTPUT:>>>
1
'''
#User function Template for python3

class Solution:
    def isNegativeWeightCycle(self, n, edges):
        
        dist = [float("inf")]*n
        dist[0] = 0
        
        for i in range(n-1):
            updated = False
            for u,v,w in edges:
                if dist[v] > dist[u] + w:
                    
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                return 0
            
        for u,v,w in edges:
            if dist[v] > dist[u] + w:
                return 1        
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.isNegativeWeightCycle(n, edges)
        print(ans)

# } Driver Code Ends