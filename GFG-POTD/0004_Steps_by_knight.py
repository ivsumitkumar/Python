'''
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.

Note:
The initial and the target position co-ordinates of Knight have been given accoring to 1-base indexing.

 

Example 1:

Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:

Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
 

 

Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the inital position of Knight (KnightPos), the target position of Knight (TargetPos) and the size of the chess board (N) as an input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position.

 

Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(N2).

 

Constraints:
1 <= N <= 1000
1 <= Knight_pos(X, Y), Targer_pos(X, Y) <= N

SAMPLE INPUT:>>
1
6
4 5
1 1
EXPECTED OUTPUT:>>
3

'''

class cell:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


class Solution:
    def isInside(self, x, y, N):
        if x >= 0 and x <= N and y >= 0 and y <= N:
            return True
        return False

    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        queue = []
        queue.append(cell(KnightPos[0], KnightPos[1], 0))
        visited = [[False for j in range(N+1)] for i in range(N+1)]
        visited[KnightPos[0]][KnightPos[1]] = True
        while len(queue) > 0:
            front = queue[0]
            queue.pop(0)
            if front.x == TargetPos[0] and front.y == TargetPos[1]:
                return front.dist
            for i in range(8):
                x = front.x+dx[i]
                y = front.y+dy[i]
                if self.isInside(x, y, N) and not visited[x][y]:
                    visited[x][y] = True
                    queue.append(cell(x, y, front.dist+1))

#{ 
#  Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends