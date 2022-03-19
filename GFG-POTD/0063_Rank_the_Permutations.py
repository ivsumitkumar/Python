'''
LEvel:>>> Medium
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 

Example 1:

Input:
S = "abc"
Output:
1
Explanation:
The order permutations with letters 
'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
Example 2:

Input:
S = "acb"
Output:
2

Your Task:
You don't need to read input or print anything. Your task is to complete the function findRank() which takes the string S as input parameter and returns the rank of the string amongst its permutations.
It is guaranteed no characters are repeated in the string.


Expected Time Complexity: O(|S|*26)
Expected Auxiliary Space: O(|S|)
Note: |S| represents the length of string S.


Constraints:
1 ≤ |S| ≤ 18

Related Topics:>>>
Number-theory
Strings

SAMPLE INPUT:>>>
1
abc
OUTPUT:>>>
1
'''
#User function Template for python3

class Solution:
    def findRank(self, s):
        #Code 
        factorial = [0 for _ in range(27)]
        factorial[1] = 1
        for i in range(2,27):
            factorial[i] = factorial[i-1]*i
        arr = [0 for i in range(27)]
        for c in s:
            arr[ord(c)-ord('a')] = 1
        rank = 0 
        for i in range(len(s)):
            countl = 0
            for j in range(27):
                if ord(s[i])-ord('a') == j:
                    break
                elif arr[j]:
                    countl+= 1
            arr[ord(s[i])-ord('a')] = 0
            rank += countl*factorial[len(s)-1-i]
        return rank+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input().strip()
        obj = Solution()
        ans = obj.findRank(str)
        print(ans)
# } Driver Code Ends