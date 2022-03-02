'''
LEVEL:>>> Medium
Given a string S containing lowercase english alphabet characters. The task is to calculate the number of distinct strings that can be obtained after performing exactly one swap.
In one swap,Geek can pick two distinct index i and j (i.e 1 < i < j < |S| ) of the string, then swap the characters at the position i and j.

 

Example 1:

Input:
S = "geek"
Output: 
6
Explanation: 
After one swap, There are only 6 distinct strings 
possible.(i.e "egek","eegk","geek","geke","gkee" and 
"keeg")
 

Example 2:

Input:
S = "ab"
Output: 
1
Explanation:
Only one string is possible after one swap(i.e "ba")
 

Your Task: 
You don't need to read input or print anything. Complete the function countStrings( ) which takes the string S as input parameters and returns the required answer.

 

Expected Time Complexity: O(|S|) .
Expected Auxiliary Space: O(1) .

 

Constraints:
2 ≤ |S| ≤ 105
S contains lowercase characters

Related Topics:>>>
Strings

SAMPLE INPUT:>>>
1
geek
OUTPUT:>>> 6
'''
#User function Template for python3
class Solution:
    def countStrings(self, S): 
        n = len(S)
        charSet = {}
        count = 0
        for i in S:
            if i in charSet:
                count = count + charSet[i] + 1
                charSet[i] += 1
            else:
                charSet[i] = 0
        ans = (n*(n-1)) // 2
        if(count >0):
            ans = ans - count + 1
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends