'''
LEVEL:>>> Medium

Given a positive integer N, return its corresponding column title as it would appear in an Excel sheet.
For N =1 we have column A, for 27 we have AA and so on.

Note: The alphabets are all in uppercase.

Example 1:

Input:
N = 51
Output: AY
Your Task:
Complete the function ExcelColumn() which takes N as input and returns output string.

Expected Time Complexity: O(Log(N))
Expected Auxiliary Space: O(Log(N))

Constraints:
1 ≤ N ≤ 107

RELATED TOPICS:>>>  Strings

SAMPLE INPUT:>>>
1
51 
OUTPUT:>>> AY

SAMPLE INPUT:>>>
1
26
OUTPUT:>>> Z
'''
#User function Template for python3
import string
class Solution:
    def ExcelColumn(self, N):
        #return required string
        #code here
        letter = string.ascii_uppercase
        p=[]
        while(N>0):
            p.insert(0,letter[(N%26)-1])
            if N%26==0:
                N = N//26 - 1
            else:
                N = N//26
        return ''.join(p)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends