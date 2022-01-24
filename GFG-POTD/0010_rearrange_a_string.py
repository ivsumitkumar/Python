'''
Given a string containing uppercase alphabets and integer digits (from 0 to 9), the task is to print the alphabets in the lexicographical order followed by the sum of digits.

Example 1:

Input: S = "AC2BEW3"
Output: "ABCEW5"
Explanation: 2 + 3 = 5 and we print all
alphabets in the lexicographical order. 
Example 2:

Input: S = "ACCBA10D2EW30"
Output: "AABCCDEW6"
Explanation: 0+1+2+3 = 6 and we print all
alphabets in the lexicographical order. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function arrangeString() which takes the string S as inputs and returns the modified string.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(26)

Constraints:
1 ≤ |S| ≤ 105
S contains only upper case alphabets and digits.

Related Topics:>>  Strings

SAMPLE INPUT:>>
1
ACCBA10D2EW30
OUTPUT:>> AABCCDEW6

SAMPLE INPUT:>>
1
AC2BEW3
OUTPUT:>> ABCEW5
'''
class Solution:
    def arrangeString(self, s):
        # code here
        ls,ln,t,st,result=[],[],0,"",0
        for i in s:
            if i.isdigit():
                ln.append(int(i))
            else:
                ls.append(i)
        ls.sort()
        for j in range(len(ln)):
            t+=ln[j]
        for k in ls:
            st+=k
        result= st+str(t)
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends