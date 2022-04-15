'''
LEVEL:>>> Medium
Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.

Example 1:

Input:
R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
Output:
29
Explanation:
The matrix is as follows and the
blue rectangle denotes the maximum sum
rectangle.
Thumbnail
Example 2:

Input:
R=2
C=2
M=[[-1,-2],[-3,-4]]
Output:
-1
Explanation:
Taking only the first cell is the 
optimal choice.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maximumSumRectangle() which takes the number R, C, and the 2D matrix M as input parameters and returns the maximum sum submatrix.


Expected Time Complexity:O(R*R*C)
Expected Auxillary Space:O(R*C)
 

Constraints:
1<=R,C<=500
-1000<=M[i][j]<=1000

Related Topics:>>>
 Kadane 
 Matrix 
 Prefix-sum

SAMPLE INPUT:>>>
1
4 5
1 2 -1 -4 -20
-8 -3 4 2 1
3 8 10 1 3
-4 -1 1 7 -6

OUTPUT:>>>
29
'''
class Solution:
    def kadanes(self,arr, n):
        s, maxi = arr[0], arr[0]
        for i in range(1,n):
            s += arr[i]
            s = max(s,arr[i])
            maxi = max(s,maxi)
        return maxi
        
        
    def maximumSumRectangle(self,R,C,M):
        #code here
        res = M[0][0]
        for starti in range(R):
            subMatSum = [0 for _ in range(C)]
            for i in range(starti, R):
                for j in range(C):
                    subMatSum[j] += M[i][j]
                res = max(res, self.kadanes(subMatSum, C))
        return res