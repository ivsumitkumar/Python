'''
LEVEL:>>> Medium
Given a list of coins of distinct denominations and total amount of money. Find the minimum number of coins required to make up that amount. Output -1 if that money cannot be made up using given coins.
You may assume that there are infinite numbers of coins of each type.
 

Example 1:

Input: arr = [1, 2, 5], amount = 11
Output: 3
Explanation: 2*5 + 1 = 11. So taking 2 
denominations of 5 and 1 denomination of  
1, one can make 11.
Example 2:

Input: arr = [2, 6], amount = 7
Output: -1
Explanation: Not possible to make 7 using 
denominations 2 and 6.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function MinCoin() which takes list of denominations and amount as input parameter and returns miimum number of coins to make up amount. If not possible returns -1.
 

Expected Time Complexity: O(n*amount)
Expected Space Complexity: O(amount)
 

Contstraints:
1 <= number of distinct denominations <= 100
1 <= amount <= 10^4

Related Topics:>>>
Dynamic Programming
Greedy

SAMPLE INPUT:>>>
1
3 11
1 2 5

OUTPUT:>>> 3
'''
#User function Template for python3

class Solution:
    def MinCoin(self, nums, amount):
        # Code here
        dp = [None for i in range(amount+1)]
        dp[0] = []
        for i in range(amount+1):
            if dp[i] is not None:
                for num in nums:
                    combination = [*dp[i], num]
                    if i + num <= amount:
                        if dp[i+num] is None or len(dp[i+num]) > len(combination):
                            dp[i+num] = combination
        if dp[amount] is None:
            return -1
        else:
            return len(dp[amount])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, amount = input().split()
        n = int(n)
        amount = int(amount)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.MinCoin(nums, amount)
        print(ans)
# } Driver Code Ends