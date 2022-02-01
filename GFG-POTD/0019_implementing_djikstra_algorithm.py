'''
LEVEL:>>> Medium
Given a weighted, undirected and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
Note: The Graph doesn't contain any negative weight cycle.

 

Example 1:

Input:

S = 0
Output:
0 9
Explanation:
The source vertex is 0. Hence, the shortest 
distance of node 0 is 0 and the shortest 
distance from node 9 is 9 - 0 = 9.
 

Example 2:

Input:

S = 2
Output:
4 3 0
Explanation:
For nodes 2 to 0, we can follow the path-
2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So,
the Shortest path from 2 to 0 is 4.
The other distances are pretty straight-forward.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function dijkstra()  which takes number of vertices V and an adjacency list adj as input parameters and returns a list of integers, where ith integer denotes the shortest distance of the ith node from Source node. Here adj[i] contains a list of lists containing two integers where the first integer j denotes that there is an edge between i and j and second integer w denotes that the weight between edge i and j is w.

 

Expected Time Complexity: O(V2).
Expected Auxiliary Space: O(V2).

 

Constraints:
1 ≤ V ≤ 1000
0 ≤ adj[i][j] ≤ 1000
1 ≤ adj.size() ≤ [ (V*(V - 1)) / 2 ]
0 ≤ S < V

Related Topics:>>> 
Graph
Algorithms

Input Format:

First line of the custom input must contain two space separated integers V denoting the number of vertices and E denoting the number of edges. Next E lines contains three space-separated integers denoting each edge and weight between the edges. Last line contains an integer S denoting the Source of the graph.

SAMPLE INPUT:>>>
1
2 1
0 1 9
0
OUTPUT:>>> 0 9

SAMPLE INPUT:>>>
1
3 3
0 1 1
0 2 6
1 2 3
2
OUTPUT:>>> 4 3 0
'''
import sys

class Solution:

   #Function to find the shortest distance of all the vertices
   #from the source vertex S.
   def dijkstra(self, V, adj, S):
       #code here
       result = [sys.maxsize] * V
       result[S] = 0
       queue = []
       queue.append(S)
       while queue:
           vertex = queue.pop(0)
           for neighbour in adj[vertex]:
               adj_vertex = neighbour[0]
               adj_distance = neighbour[1]
               if result[vertex] + adj_distance < result[adj_vertex]:
                   result[adj_vertex] = result[vertex] + adj_distance
                   queue.append(adj_vertex)
       return result
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends