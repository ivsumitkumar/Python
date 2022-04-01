'''
LEVEL:>>> Medium
Given a sequence of non-negative integers, find the subsequence of length 3 having maximum product, with the elements of the subsequence being in increasing order.

 

Example 1:

â€‹Input:
n = 8
arr[ ] = {6, 7, 8, 1, 2, 3, 9, 10}
Output:
8 9 10
Explanation: 3 increasing elements of 
the given arrays are 8,9 and 10 which 
forms the subsequence of size 3 with 
maximum product.

â€‹Example 2:

Input:
n = 4
arr[ ] = {3, 4, 2, 1} 
Output:
Not Present 
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function maxProductSubsequence() that takes an array arr, sizeOfArray n, and return the subsequence of size 3 having the maximum product, numbers of subsequence being in increasing order. If no such sequence exists, return "-1". The driver code takes care of the printing.


Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(N).



Constraints:
1 <= N <= 10^5
1 <= Arr[i] <= 10^5

Related Topics:>>>
Arrays
Sorting

SAMPLE INPUT:>>>
1
8
6 7 8 1 2 3 9 10

OUTPUT:>>>
8 9 10
'''
#User function Template for python3

#Feeling lazy else I would have implemented my own bisect_left
from bisect import bisect_left as bl
class Solution:
   
   def binPartition(self,a, value):
       return bl(a, value)-1
       


   def countArray (self, a, n) : 
       if n<3:
           return [-1]
       left=[-1,a[0]]
       result=[-1]
       right=max(a[1:])
       maxproduct=-1
       for i in range(1,n-1):
           current=a[i]
           if current>=right:
               right=max(a[i+1:])
           #print(current)
           j=self.binPartition(left,current)
           
           
           leftValue=left[j]
           left.insert(j+1,current)#=left[:j+1] + [current] + left[j+1:]
           #left.append(current)
           #left.sort()
           rightValue=right
           #print([leftValue,current,rightValue])
           if not(leftValue<current and current<rightValue):
               continue
           currentprod=leftValue*rightValue*current
           if currentprod>maxproduct:
               maxproduct=currentprod
               result=[leftValue,current,rightValue]
           
           
       return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = Solution().countArray(arr, n)
    if(ans[0] == -1):
        print("Not Present")
    else:
        print(*ans)
# } Driver Code Ends