'''
LEVEL:>>> EASY
Given an array Arr of size N and a positive integer K, find the sub-array of length K with the maximum average.


Example 1:

Input:
K = 4, N = 6
Arr[] = {1, 12, -5, -6, 50, 3}
Output: 12 -5 -6 50
Explanation: Maximum average is 
(12 - 5 - 6 + 50)/4 = 51/4.

Example 2:

Input:
K = 3, N = 7
Arr[] = {3, -435, 335, 10, -50, 100, 20}
Output: 335 10 -50
Explanation: Maximum average is 
(335 + 10 - 50)/3 = 295/3.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxAverage() which takes the array of integers arr, its size n and integer k as input parameters and returns an integer denoting the starting index of the subarray.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints
1 <= N <= 105
0 <= |Arr[i]| <= 103

Related Topics:>>>
Arrays

SAMPLE INPUT:>>>
1
5
13
-209 336 -126 -480 96 -479 -152 -301 168 -16 -219 234 -447
OUTPUT:>>> 
-301 168 -16 -219 234
'''
#User function Template for python3

class Solution:
    def findMaxAverage(self, arr, n, k):
        # code here
        # maximum sum subarray of length k
        l = 0 
        currsum = 0
        for i in range(k):
            currsum += arr[i]
        ans = currsum
        out = 0
        for j in range(k,n):
            currsum -= arr[l]
            l+=1
            currsum += arr[j]
            if currsum > ans:
                ans = currsum
                out = l
        return out

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends