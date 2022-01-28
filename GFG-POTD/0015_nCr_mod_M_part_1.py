'''
LEVEL:>> Hard

Given 2 integers n and r. You task is to calculate nCr%1000003.
 

Example 1:

Input: n = 5, r = 2
Output: 10
Explanation: 5C2 = 5! / (2! * 3!) = 10
Example 2:

Input: n = 3, r = 2
Output: 3
Explanation: 3C2 = 3! / (2! * 1!) = 3
 

Your Task:
You don't need to read or print anything. Your task is to complete the function nCr() which takes n and r as input parameter and returns nCr modulo 1000003.
 

Expected Time Complexity: O(m * logmn) where m = 1000003
Expected Space Complexity: O(m)
 

Constraints:
1 <= n <= r <= 1016

Related Topics:>>>
Combinatorial
Modular Arithmetic

SAMPLE INPUTS:>>>
1
5 2
OUTPUT:>>> 10

SAMPLE INPUTS:>>>
1
3 2
OUTPUT:>>> 3
'''
#User function Template for python3
import math

class Solution:
    def nCr(self, n, r):
        # Code here
        # pn = math.factorial(n)
        # pr = math.factorial(r)
        # nr = math.factorial(abs(n-r))
        ncr = math.factorial(n)/(math.factorial(r)*math.factorial(abs(n-r)))
        return int(ncr%1000003)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, r = input().split()
        n = int(n)
        r = int(r)
        obj = Solution()
        ans = obj.nCr(n, r)
        print(ans)


# } Driver Code Ends