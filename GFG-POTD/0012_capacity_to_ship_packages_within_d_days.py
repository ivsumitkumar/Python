'''
LEVEL:>> HARD

Given an array arr[] of N weights. Find the least weight capacity of a boat to ship all weights within D days.
The ith weight has a weight of arr[i]. Each day, we load the boat with weights given by arr[i].We may not load more weight than the maximum weight capacity of the ship.

Note: You have to load weights on the boat in the given order.

 

Example 1:

Input:
N = 3
arr[] = {1, 2, 1}
D = 2
Output:
3
Explanation:
We can ship the weights in 2 days
in the following way:-
Day 1- 1,2
Day 2- 1
Example 2:
Input:
N = 3
arr[] = {9, 8, 10}
D = 3
Output:
10
Explanation:
We can ship the weights in 3 days
in the following way:-
Day 1- 9
Day 2- 8
Day 3- 10
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function leastWeightCapacity() which takes 2 integers N, and D, and an array arr of size N as input and returns the least weight capacity of the boat required.


Expected Time Complexity: O(N*log(Sum of weights - max(list of weights))
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ D ≤ N ≤ 105
1 ≤ arr[i] ≤ 500

Related Topics:>>
 Binary Search
 Arrays

SAMPLE INPUT:>>
1
3
1 2 1
2
OUTPUT:>> 3

SAMPLE INPUT:>>
1
3
9 8 10
3
OUTPUT:>> 10
'''
#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, N, D):
        # code here 
        
        def helper(capacity):
            prev = 0
            ans = 0
            for num in arr:
                prev += num
                if prev > capacity:
                    ans += 1
                    prev = num
                    
            return ans + 1 if prev > 0 else ans
            
        start = max(arr) - 1
        end = sum(arr)
        
        while end - start > 1:
            m = (end + start) //2
            if helper(m) <= D:
                end = m
            else:
                start = m
                
                
        return end

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends