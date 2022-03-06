'''
LEVEL:>>>Medium
For a given 2D Matrix before, the corresponding cell (x, y) of the after matrix is calculated as follows: 

res = 0;
for(i = 0; i <= x; i++){
    for( j = 0; j <= y; j++){              
        res += before(i,j);
    }
}
after(x,y) = res;
Given an N*M 2D-Matrix after, your task is to find the corresponding before matrix for the given matrix.

 

Example 1:

Input:
N = 2, M = 3
after[][] = {{1, 3, 6},
            {3, 7, 11}}
Output:
1 2 3
2 2 1
Explanation:
The before matrix for the given after matrix
matrix is {{1, 2, 3}, {2, 2, 1}}.
Example 2:

Input: 
N = 1, M = 3
after[][] = {{1, 3, 5}}
Output:
1 2 2
Explanation: 
The before matrix for the given after matrix
is {{1, 2, 2}}.
Your Task:
Complete the function computeBeforeMatrix() which takes the integers N, M, and the 2D Matrix after as the input parameters, and returns the before matrix of the given after matrix.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N, M, after[i][j]  ≤  109

Related Topics:>>>
Matrix
Prefix-sum

SAMPLE INPUT:>>>
1
2 3
1 3 6
3 7 11

OUTPUT:>>>
1 2 3 
2 2 1 
'''
#User function Template for python3

class Solution:
   def computeBeforeMatrix(self, N, M, after):
      
       for i in range(N-1,-1,-1):
           for  j in range(M-1,-1,-1):
               
               if(i):
                   after[i][j]-=after[i-1][j]
               if(j):
                   after[i][j]-=after[i][j-1]
               
               if(i and j):
                   after[i][j]+=after[i-1][j-1]
           
       return after

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, M =[int(i) for i in input().split()]
        after= []
        for j in range (N):
            after.append([int(i) for i in input().split()])
        ob = Solution()
        before=ob.computeBeforeMatrix(N,M,after)
        for i in range(len(before)): 
            for j in range(len(before[i])):
                print(before[i][j],end=' ')
            print()
        
        
        T -= 1
# } Driver Code Ends