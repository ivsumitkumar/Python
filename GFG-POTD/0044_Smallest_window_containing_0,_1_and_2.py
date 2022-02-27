'''
LEVEL:>>> Easy
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Example 1:

Input:
S = "01212"
Output:
3
Explanation:
The substring 012 is the smallest substring
that contains the characters 0, 1 and 2.
Example 2:

Input: 
S = "12121"
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
Your Task:
Complete the function smallestSubstring() which takes the string S as input, and returns the length of the smallest substring of string S that contains all the three characters 0, 1 and 2.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 105
All the characters of String S lies in the set {'0', '1', '2'}

Related Topics:>>>
 Sliding-window
 Strings
 Two-pointer-algorithm

SAMPLE INPUT:>>>
1
1210
OUTPUT:>>> 3
'''
#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        arr = [-1, -1, -1]
        ans = float("inf")
        
        for i in range(len(S)):
            mn = min(arr)
            mx = max(arr)
            arr[int(S[i])] = i
            if mn != -1:
                ans = min(ans, mx - mn)
        
        mn = min(arr)
        mx = max(arr)
        if mn != -1:
            ans = min(ans, mx - mn)
        
        return -1 if ans == float('inf') else ans + 1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.smallestSubstring(S)
        
        print(ans)



# } Driver Code Ends