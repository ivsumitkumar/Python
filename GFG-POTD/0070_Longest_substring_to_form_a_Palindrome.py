'''
LEVEL:>>> HARD
Given a string S which only contains lowercase alphabets. Find the length of the longest substring of S such that the characters in it can be rearranged to form a palindrome.


Example 1:

Input:
S = "aabe"
Output:
3
Explanation:
The substring "aab" can be rearranged to
"aba" which is the longest palindrome
possible for this String.
Example 2:
Input:
S = "adbabd"
Output:
6
Explanation:
The whole string “adbabd” can be
rearranged to form a palindromic substring.
One possible arrangement is "abddba".
Thus, output length of the string is 6. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function longestSubstring() which takes a String S as input and returns the length of largest possible Palindrome.


Expected Time Complexity: O(|S|*26)
Expected Auxiliary Space: O(|S|*26)


Constraints:
1 ≤ |S| ≤ 10^5

Related Topics:>>>
 Strings
 Palindrome
 Dynamic Programming
 
SAPMLE INPUT:>>>
1
aabe
OUTPUT:>>>
3
'''
#User function Template for python3

class Solution:
    def longestSubstring(self, s):
        d = {}
        d[0] =  -1
        x=ans = 0
        for i in range(len(s)):
            x = x ^ (1 << (ord(s[i])-ord('a')))
            if x in d:
                ans = max(ans,i-d[x])
            else:
                d[x] = i
            for j in range(0,26):
                m = x ^ (1<<j)
                if m in d:
                    ans = max(ans,i-d[m])
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S))
# } Driver Code Ends