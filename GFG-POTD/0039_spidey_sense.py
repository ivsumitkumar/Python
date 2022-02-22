'''
Level:>>> Medium
Spiderman is stuck in a difficult situation. His arch-enemy the Green Goblin has planted several of his infamous Pumpkin Bombs in various locations in a building. Help Spiderman activate his Spidey Sense and identify the impact zones. 
He has a blueprint of the building which is a M x N matrix that is filled with the characters O, B, and W where: 
O represents an open space.
B represents a bomb.
W represents a wall.
You have to replace all of the Os (open spaces) in the matrix with their shortest distance from a bomb without being able to go through any walls. Also, replace the bombs with 0 and walls with -1 in the resultant matrix. If no path exists between a bomb and an open space replace the corresponding 'O' with -1.

Example 1:

Input: N = 3, M = 3
A[] = {{O, O, O}, 
       {W, B, B}, 
       {W, O, O}}
Output: {{2, 1, 1}, 
         {-1, 0, 0},  
         {-1, 1, 1}}
Explanation: The walls at (1,0) and (2,0) 
are replaced by -1. The bombs at (1,1) and 
(1,2) are replaced by 0. The impact zone 
for the bomb at (1,1) includes open spaces 
at index (0,0), (0,1) and (2,1) with distance 
from bomb calculated as 2,1,1 respectively.
The impact zone for the bomb at (1,2) 
includes open spaces at index (0,3) and (2,2) 
with distance from bomb calculated as 1,1 
respectively.

Example 2:

IInput: N = 2, M = 2
A[] = {{O, O},
       {O, O}} 
Output: {{-1, -1}
         {-1, -1}
Your Task:  
You don't need to read input or print anything. Complete the function findDistance() which takes the matrix A[], M, and N as input parameters and the resultant matrix

Expected Time Complexity: O(M*N)
Expected Auxiliary Space: O(M*N)


Constraints:
1 ≤ N*M ≤ 106

Related Topics:>>>
BFS
Queue
Graph

SAMPLE INPUT:>>>
1
3 3
O O O
W B B
W O O
OUTPUT:>>>
2 1 1 
-1 0 0 
-1 1 1 
'''
from collections import deque


class Solution:
    def findDistance(self, matrix, m, n):
        # Your code goes here
        # bfs
        def issafe(ith, jth):
            if ith >= 0 and ith < len(matrix) and jth>=0 and jth < len(matrix[0])\
            and visited[ith][jth] == False and matrix[ith][jth] == "O":
                return True
            return False

        q = deque()
        visited = [[False for i in range(len(matrix[0]))]
                   for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'W':
                    matrix[i][j] = -1
                elif matrix[i][j] == 'B':
                    q.append([i, j])
        moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        level = -1
        while (q):
            size = len(q)
            level += 1
            while (size):
                ele = q.popleft()
                if matrix[ele[0]][ele[1]] == "O":
                    matrix[ele[0]][ele[1]] = level
                visited[ele[0]][ele[1]] = True
                if matrix[ele[0]][ele[1]] == 'B':
                    matrix[ele[0]][ele[1]] = 0
                for move in moves:
                    if issafe(ele[0] + move[0], ele[1] + move[1]):
                        q.append([ele[0] + move[0], ele[1] + move[1]])
                size -= 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'O':
                    matrix[i][j] = -1
        return matrix


#{
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        m = int(size[0])
        n = int(size[1])
        matrix = []
        for _ in range(m):
            matrix.append([x for x in input().strip().split()])
        obj = Solution()
        result = obj.findDistance(matrix, m, n)
        for i in result:
            for j in i:
                print(j, end=' ')
            print()
# } Driver Code Ends