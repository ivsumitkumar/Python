'''
LEVEL:>> Medium

In Geekland there is a grid of coins of size N x N. You have to find the maximum sum of coins in any sub-grid of size K x K.
Note: Coins of the negative denomination are also possible at Geekland.

Example 1:

Input: N = 5, K = 3 
mat[[]] = {1, 1, 1, 1, 1} 
          {2, 2, 2, 2, 2} 
          {3, 8, 6, 7, 3} 
          {4, 4, 4, 4, 4} 
          {5, 5, 5, 5, 5}
Output: 48
Explanation: {8, 6, 7}
             {4, 4, 4}
             {5, 5, 5}
has the maximum sum

Example 2:

Input: N = 1, K = 1
mat[[]] = {{4}} 
Output: 4
Your Task:  
You don't need to read input or print anything. Complete the function Maximum_Sum() which takes the matrix mat[], size of Matrix N, and value K as input parameters and returns the maximum sum.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N2)

Constraints:
1 ≤ K ≤ N ≤ 103
-5*105 ≤ mat[i][j] ≤ 5*105

Related Topics:>>>
Arrays
Matrix

SAMPLE INPUTS:>>>
1
5
1 1 1 1 1
2 2 2 2 2
3 8 6 7 3
4 4 4 4 4
5 5 5 5 5
3
OUTPUT:>>> 48
SAMPLE INPUTS:>>>
1
1
4
1
OUTPUT:>>> 4
'''
#User function Template for python3

class Solution:
   def Maximum_Sum(self, mat, N, K):
       # Your code goes here
       maximum_sum=0
       dp=[[0 for _ in range(n+1)]for _ in range(n+1)]
       for i in range(n+1):
           for j in range(n+1):
               if (i==0 or j==0):
                   dp[i][j]=0
               else:
                   dp[i][j]=mat[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
               if (i>=k and j>=k):
                   maximum_sum=max(dp[i][j]-(dp[i][j-k]+dp[i-k][j]-dp[i-k][j-k]),maximum_sum)
       return maximum_sum

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        matrix=[]
        for _ in range(n):
            matrix.append( [ int(x) for x in input().strip().split() ] )
        k=int(input())
        obj = Solution()
        print(obj.Maximum_Sum(matrix,n,k))
# } Driver Code Ends