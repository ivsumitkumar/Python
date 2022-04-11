'''
LEVEL:>>> Hard
Geek is in a maze of size N * M. Each cell in the maze is made of either '.' or '#'. An empty cell is represented by '.' and an obstacle is represented by '#'. If Geek starts at cell (R, C), find how many different empty cells he can pass through while avoiding the obstacles. He can move in any of the four directions but he can move up at most U times and he can move down atmost D times.

 

Example 1:

Input: 
N = 3, M = 3
R = 1, C = 0
U = 1, D = 1
mat = {{'.', '.', '.'},
       {'.', '#', '.'},
       {'#', '.', '.'}}
Output: 5
Explanation: Geek can reach 
(1, 0), (0, 0), (0, 1), (0, 2), (1, 2) 


Example 2:

Input: 
N = 3, M = 4
R = 1, C = 0
U = 1, D = 2 
mat = {{'.', '.', '.'}, 
       {'.', '#', '.'}, 
       {'.', '.', '.'},
       {'#', '.', '.'}} 
Output: 10
Explanation: Geek can reach all the 
cells except for the obstacles.
 

Your Task:  
You don't need to read input or print anything. Complete the function numberOfCells() which takes N, M, R, C, U, D and the two dimensional character array mat[][] as input parameters and returns the number of cells geek can visit( If he is standing on obstacle he can not move).


Constraints:
1 ≤ N*M ≤ 10^6
mat[i][j] = '#" or '.'
0 ≤ R ≤ N-1
0 ≤ C ≤ M-1

Related Topics:>>>
Graph

SAMPLE INPUT:>>>
1
3 3 1 0 1 1
...
.#.
#..
OUTPUT:>>>
5
'''
#User function Template for python3

class Solution:
    def numberOfCells(self,n,m,r,c,u,d,mat):
        if mat[r][c] != ".":
            return 0
        visited = {(r,c)}
        coord = [(r,c,u,d)]

        def check(row, col):
            if row>=0 and row < n and col >= 0 and col < m and \
            (row,col) not in visited and mat[row][col] == ".":
                visited.add((row,col))
                return True
            return False
        
        while coord:
            coord2 = []
            while coord:
                i,j,up,down=coord.pop()
                if check(i,j-1):
                    coord.append((i,j-1,up, down))
                if check(i,j+1):
                    coord.append((i,j+1,up, down))
                if up > 0 and check(i-1,j):
                    coord2.append((i-1,j,up-1, down))
                if down > 0 and check(i+1,j):
                    coord2.append((i+1,j,up,down-1))
            coord = coord2
        return len(visited)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(int(input()))

    for tcs in range(t):

        n, m, r, c, u, d = [int(x) for x in input().split()]

        mat = []

        for i in range(n):
            matele = [x for x in input()]
            mat.append(matele)
        obj=Solution()
        print(obj.numberOfCells(n, m, r, c, u, d, mat))
# } Driver Code Ends