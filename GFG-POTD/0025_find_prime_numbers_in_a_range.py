'''
LEVEL:>>> Medium
Given two integers M and N, generate all primes between M and N.

Example 1:

Input:
M=1,N=10
Output:
2 3 5 7
Explanation:
The prime numbers between 1 and 10
are 2,3,5 and 7.
Example 2:

Input:
M=2, N=5
Output:
2,3,5
Explanation:
The prime numbers between 2 and 5 are 
2,3 and 5.

Your Task:
You don't need to read input or print anything. Your task is to complete the function primeRange() which takes 2 integer inputs M and N and returns a list of all primes between M and N.


Expected Time Complexity:O(N*sqrt(N))
Expected Auxillary Space:O(1)


Constraints:
1<=M<=N<=106

Related Topics:>>>
Prime Numbers

SAMPLE INPUT:>>>
1
1 10
OUTPUT:>>> 2 3 5 7

SAMPLE INPUT:>>>
1
1 50
OUTPUT:>>>
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

'''
#User function Template for python3

class Solution:        
    def primeRange(self,M,N):
        #code here
        primenumber = []
        for i in range(M, N+1):
            if i > 1:
                for x in range(2, int(math.sqrt(i)+1)):
                    if i % x == 0:
                        break
        
                else:
                    primenumber.append(i)
        return primenumber

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends