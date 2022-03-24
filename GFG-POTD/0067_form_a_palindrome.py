'''
LEVEL:>>> Medium
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

Example 1:

Input:
abcd
Output:
3
Explanation:
Here we can append 3 characters in the 
beginning,and the resultant string will 
be a palindrome ("dcbabcd").
Example 2:

Input:
aba
Output:
0
Explanation:
Given string is already a pallindrome hence
no insertions are required.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMinInsertions() which takes string S as input parameters and returns minimimum numser of insertions required.

Expected Time Complexity: O(|S|2)
Expected Auxiliary Space: O(|S|2)

Constraints:
1 ≤ |S| ≤ 500

Related Topics:>>>>
Dynamic Programming
Strings

SAMPLE INPUT:>>>
1
abcd
OUTPUT:>>> 3
'''
#User function Template for python3

class Solution:
    def lcs(self,s,s1):
        dp=[[0 for i in range(len(s)+1)]for j in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                if(i==0 or j==0):
                    continue
                if(s[i-1]==s1[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
    def findMinInsertions(self, s):
        return len(s)-self.lcs(s,s[::-1])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.findMinInsertions(S))
# } Driver Code Ends