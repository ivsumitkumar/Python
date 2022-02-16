'''
Level:>>> Medium
Given a NxM binary matrix consisting of 0s and 1s. Find if there exists a rectangle/ square within the matrix whose all four corners are 1. 

Example 1:

Input:
N = 4, M = 5
matrix[][] = 
{
{1 0 0 1 0},
{0 0 1 0 1},
{0 0 0 1 0}, 
{1 0 1 0 1}
} 

Output: Yes
Explanation:
Valid corners are at index (1,2), (1,4), (3,2), (3,4) 
Example 2:

Input:
N = 3, M = 3
matrix[][] = 
{{0 0 0},
{0 0 0},
{0 0 0}}
Output: No
Your Task:
You don't need to take input or print anything. Complete the function ValidCorners() that takes the given matrix as input parameter and returns a boolean value.

Constraints:
1 <= R, C <= 200
0 <= A[i] <= 1

Related Topics:>>>
Matrix

SAMPLE INPUT:>>>
1
4
5
1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 
OUTPUT:>>> YES
'''
#User function Template for python3

class Solution:    
    def ValidCorner(self,matrix): 
        # Your code goes here 
        N=len(matrix)
        M=len(matrix[0])
        
        dict_matrix = {}
        
        for i in range(N):
            arr_row = []
            for j in range(M):
                if matrix[i][j]==1:
                    arr_row.append(j)
            dict_matrix[i] = arr_row
       
        isSquare=False
        for i in range(N):
            for j in range(i+1,N):
                if len(set(dict_matrix[i]) &                                                                             set(dict_matrix[j]))>=2:
                    isSquare=True
                    break
            if(isSquare):
                return 'Yes'

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        line = input().strip().split()
        mat = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
            for j in range(c):
                mat[i][j] = int( line[i*c+j] )
        ob=Solution()
        if (ob.ValidCorner(mat)): 
            print("Yes") 
        else: 
            print("No") 


# } Driver Code Ends