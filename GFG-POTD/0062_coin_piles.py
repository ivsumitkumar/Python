'''
Level:>>> Medium
There are N piles of coins each containing  Ai (1<=i<=N) coins. Find the minimum number of coins to be removed such that the absolute difference of coins in any two piles is at most K.
Note: You can also remove a pile by removing all the coins of that pile.


Example 1:

Input:
N = 4, K = 0
arr[] = {2, 2, 2, 2}
Output:
0
Explanation:
For any two piles the difference in the
number of coins is <=0. So no need to
remove any coins. 
Example 2:
Input:
N = 6, K = 3
arr[] = {1, 5, 1, 2, 5, 1} 
Output :
2
Explanation:
If we remove one coin each from both
the piles containing 5 coins , then
for any two piles the absolute difference
in the number of coins is <=3. 


Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSteps() which takes 2 integers N, and K and an array A of size N as input and returns the minimum number of coins that need to be removed.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 105
0 ≤ K ≤ 104
1 ≤ A[i] ≤ 103

Related Topics:>>>
Greedy
Arrays
Binary Search

SAMPLE INPUT:>>>
1
4 0
2 2 2 2
OUTPUT:>>> 0
'''
#User function Template for python3

import bisect
#User function Template for python3
class Solution:
   def minSteps(self, A, N, K):
       # code here 
       A.sort()
       pre=0
       s=sum(A)
       pre_s=[]
       for i in A:
           if len(pre_s)==0:
               pre_s.append(i)
           else:
               pre_s.append(i+pre_s[-1])
       coins=float('inf')
       for i in range(len(A)):
           if i!=0 and A[i]==A[i-1]:
               pre+=A[i]
               continue
           index=bisect.bisect_right(A,A[i]+K)
           if index>N:
               index=N
           temp=s-(pre_s[index-1])
           temp=(temp-((A[i]+K)*(N-index)))
           coins=min(coins,pre+temp)
           pre+=A[i]
       return coins

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minSteps(A,N,K))
# } Driver Code Ends