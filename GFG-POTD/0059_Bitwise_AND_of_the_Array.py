'''
LEVEL:>>> Medium
Given an array A[ ] of N integers and an integer X. In one operation, you can change the ith element of the array to any integer value where 1 ≤ i ≤ N. Calculate minimum number of such operations required such that the bitwise AND of all the elements of the array is strictly greater than X.

Example 1:

Input:
N = 4, X = 2
A[] = {3, 1, 2, 7}
Output: 
2
Explanation: 
After performing two operations:
Modified array: {3, 3, 11, 7} 
Now, Bitwise AND of all the elements
is 3 & 3 & 11 & 7 = 3 
Example 2:

Input:
N = 3, X = 1
A[] = {2, 2, 2}
Output: 
0
Your Task:
You don't need to read input or print anything. Your task is to complete the function count( ) which takes N, A[ ] and X as input parameters and returns the minimum number of operations required.

Expected Time Complexity: O(N * Log(max(A[ ])))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 109
1 ≤ X ≤ 109

View Bookmarked Problems
Topic Tags
 Bit Magic Arrays Greedy
 
 Related Topics:>>>
Bit Magic
Arrays
Greedy

SAMPLE INPUT:>>>
1
4 2
3 1 2 7
OUTPUT:>>> 2
'''
#User function Template for python3
import sys
class Solution:
    def count(self, N, A, X): 
        ans=sys.maxsize
        m=0
        for i in range(31,-1,-1):
            if((X>>i)&1):
                m|=(1<<i)
                continue
            count=0
            temp=m|(1<<i)
            for i in range(N):
                if((A[i]&temp)==temp):
                    count+=1
            ans=min(ans,N-count)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(N, A, X)
        print(ans)
# } Driver Code Ends