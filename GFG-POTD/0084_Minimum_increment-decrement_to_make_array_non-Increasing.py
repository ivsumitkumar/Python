'''
LEVEL:>>> Medium
Given an array a of length n, find the minimum number of operations required to make it non-increasing. You can select any one of the following operations and preform it any number of times on an array element.

increment the array element by 1.
decrement the array element by 1. 
Example 1:

Input:
N = 4 
array = {3, 1, 2, 1}
Output: 1
Explanation: 
Decrement array[2] by 1. 
New array becomes {3,1,1,1} which is non-increasing. 
Therefore, only 1 step is required. 

Example 2:

Input:
N = 4 
array = {3, 1, 5, 1}
Output: 4

Your Task:
You don't need to read input or print anything. Complete the function minOperations() that takes n and array a as input parameters and returns the minimum number of operations required. 

Expected time complexity: O(nlogn)
Expected space complexity: O(n)


Constraints:
1 <= n <= 10^4
1 <= a[i] <= 10^4

Related Topics:>>>
 Arrays
 Priority-queue
 
 SAMPLE INPUT:>>>
 1
 4
3 1 2 1

OUTPUT:>>>
1
'''
#User function Template for python3

import heapq
class Solution:
    def minOperations(self,a,n):
        # code here
        heap = []
        count = 0
        for i in range(n):
            if heap and heap[0] < a[i]:
                count += a[i] - heap[0]
                heapq.heappush(heap,a[i])
                heapq.heappop(heap)
            heapq.heappush(heap,a[i])
        return count



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[int(x) for x in input().strip().split()]
        obj=Solution()
        print(obj.minOperations(a,n))


# } Driver Code Ends