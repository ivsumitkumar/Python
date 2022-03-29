'''
LEVEL:>>> HARD
You have got a maze, which is a n*n Grid. Every cell of the maze contains these numbers 1, 2 or 3. 
If it contains 1 : means we can go Right from that cell only.
If it contains 2 : means we can go Down from that cell only.
If it contains 3 : means we can go Right and Down to both paths from that cell.
We cant go out of the maze at any time.
Initially, You are on the Top Left Corner of The maze(Entry). And, You need to go to the Bottom Right Corner of the Maze(Exit).
You need to find the total number of paths from Entry to Exit Point.
There may be many paths but you need to select that path which contains the maximum number of Adventure.
The Adventure on a path is calculated by taking the sum of all the cell values thatlies in the path.
 

Example 1:

Input: matrix = {{1,1,3,2,1},{3,2,2,1,2},
{1,3,3,1,3},{1,2,3,1,2},{1,1,1,3,1}}
Output: {4,18}
Explanation: There are total 4 Paths Available 
out of which The Max Adventure is 18. Total 
possible Adventures are 18,17,17,16. Of these 
18 is the maximum.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function FindWays() which takes matrix as input parameter and returns a list containg total number of ways to reach at (n, n) modulo 109 + 7 and maximum number of Adventure.
 

Expected Time Complexity: O(n2)
Expected Space Complexity: O(n2)
 

Constraints:
1 <= n <= 100

Related Topics:>>>
Dynamic Programming
Matrix

SAMPLE INPUT:>>>
1
5
1 1 3 2 1
3 2 2 1 2
1 3 3 1 3
1 2 3 1 2
1 1 1 3 1 
OUTPUT:>>>
4 18
'''
#User function Template for python3

class Solution:
    def FindWays(self, matrix):
 # Code here
        dp = [[[0,0] for _ in range(len(matrix))] for _ in range(len(matrix))]
        dp[0][0]=[1,0]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i>0 and matrix[i-1][j] in (2,3):
                    dp[i][j][0]+=dp[i-1][j][0]
                    dp[i][j][1]=max(dp[i][j][1],dp[i-1][j][1])
                if j>0 and matrix[i][j-1] in (1,3):
                    dp[i][j][0]+=dp[i][j-1][0]
                    dp[i][j][1]=max(dp[i][j][1],dp[i][j-1][1])
                if dp[i][j][0]>0:
                    dp[i][j][0]%=1000000007
                    dp[i][j][1]+=matrix[i][j]
        return dp[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            cur = list(map(int, input().split()))
            matrix.append(cur)
        obj = Solution()
        ans = obj.FindWays(matrix)
        for _ in ans:
            print(_, end = " ")
        print()

# } Driver Code Ends