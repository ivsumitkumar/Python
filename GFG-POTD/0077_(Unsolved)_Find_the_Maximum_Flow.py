'''
LEVEL:>>> HARD
Given a graph with N vertices numbered 1 to N and M edges, The task is to find the max flow from vertex 1 to vertex N.

In a flow network, the maximum flow of a path can't exceed the flow-capacity of an edge in the path.

Example 1:

Input:
N = 5, M =  4
Edges[]= { {1, 2, 1} , {3, 2, 2}, {4, 2, 3}, {2, 5, 5} }
Output:
1 
Explanation: 
1 - 2 - 3
   / \
  4   5 
1 unit can flow from 1 -> 2 - >5 
 

Example 2:

Input:
N = 4 , M = 4
Edges[] = { {1, 2, 8}, {1, 3, 10}, {4, 2, 2}, {3, 4, 3} }
Output:
5 
Explanation:
  1 - 2 
  |   |
  3 - 4
3 unit can flow from 1 -> 3 -> 4
2 unit can flow from 1 -> 2 -> 4
Total max flow from 1 to N = 3+2=5
Your Task: 
You don't need to read input or print anything. Your task is to complete the function solve() which takes the N (the number of vertices) ,M (the number of Edges) and the array Edges[] (Where Edges[i] denoting an undirected edge between Edges[i][0] and Edges[i][1] with a flow capacity of Edges[i][2] ), and returns the integer denoting the maximum flow from 1 to N.

Expected Time Complexity: O( max_flow* M)
Expected Auxiliary Space: O(N+M)

Where max_flow is the maximum flow from 1 to N

Constraints:
1 <= N,M,Edges[i][2] <= 1000
1 <= Edges[i][0],Edges[i][1] <= N

Related Topics:>>>
Graph

SAMPLE INPUT:>>>
1
5 4
1 2 1 3 2 2 4 2 3 2 5 5

OUTPUT:>>>
1
'''
#User function Template for python3
class Solution:
    def solve(self, N, M, Edges): 
        #code here
        pass

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges = []
        input_line = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([input_line[3*i],input_line[3*i+1],input_line[3*i+2]])

        ob = Solution()
        ans = ob.solve(N, M, Edges)
        print(ans)


# } Driver Code Ends