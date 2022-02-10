'''
LEVEL:>>> Medium
Given a positive number k, we need to find a minimum value of positive integer n, such that XOR of n and n+1 is equal to k. If no such n exist then print -1.


Example 1:

Input: k = 3
Output: 1
Explaination: 1 xor 2 = 3.

Example 2:

Input: k = 6
Output: -1
Explaination: There is no such n, so that, 
n xor n+1 = k.

Your Task:
You do not need to read input or print anything. Your task is to complete the function xorCal() which takes k as input parameter and returns the value of n. If there is no such , then it returns -1.


Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ k ≤ 100

Related Topics:>>>
Mathematical

SAMPLE INPUT:>>>
1
3
OUTPUT:>>> 1

SAMPLE INPUT:>>>
1
6
OUTPUT:>>> -1
'''
class Solution:
   def xorCal(self, k):
       for i in range(1,100):
           x=i^(i+1)
           if x==k:
               return i
       return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends