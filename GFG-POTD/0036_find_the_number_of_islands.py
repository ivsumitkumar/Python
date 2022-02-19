'''
LEVEL:>>> MEDIUM
Given a grid of size n*m (n is number of rows and m is number of columns grid has) consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.
 

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
Example 2:

Input:
grid = {{0,1,1,1,0,0,0},{0,0,1,1,0,1,0}}
Output:
2
Expanation:
The grid is-
0 1 1 1 0 0 0
0 0 1 1 0 1 0 
There are two islands one is colored in blue 
and other in orange.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function numIslands() which takes grid as input parameter and returns the total number of islands.
 

Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 500

RELATED TOPICS:>>>
DFS
GRAPH

SAMPLE INPUT:>>>
1
4 2
0 1
1 0
1 1
1 0
OUTPUT:>>> 1
'''
#User function Template for python3

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
from collections import deque
class Solution:
    #Function to find the number of islands.
    def isSafe(self, i, j, visited,grid):

        return (i >= 0 and i < len(grid) and 
                j >= 0 and j < len(grid[0]) and 
                not visited[i][j] and grid[i][j])
    def DFS(self, i, j, visited,grid):

        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited,grid):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited,grid)

    def numIslands(self, grid):
        #Code here
        visited = [[False for j in range(len(grid[0]))]for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (int(grid[i][j]) == 1) and visited[i][j] == False:
                    self.DFS(i, j, visited,grid)
                    count += 1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends