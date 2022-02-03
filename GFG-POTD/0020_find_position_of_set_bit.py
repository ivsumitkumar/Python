'''
LEVEL:>>> Basic
Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.

Example 1:

Input:
N = 2
Output:
2
Explanation:
2 is represented as "10" in Binary.
As we see there's only one set bit
and it's in Position 2 and thus the
Output 2.
Example 2:

Input:
N = 5
Output:
-1
Explanation:
5 is represented as "101" in Binary.
As we see there's two set bits
and thus the Output -1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findPosition() which takes an integer N as input and returns the answer.

Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 108

Related Topics:>>> Magic

SAMPLE INPUT:>>>
1
2
OUTPUT:>>> 2

SAMPLE INPUT:>>>
1
5
OUTPUT:>>> -1

'''
#User function Template for python3

class Solution:
    def findPosition(self, N):
        # code here
        if N==0:
            return -1
        b = bin(N).replace("0b",'')
        if b.count('1')>1 or b.count('1')==0:
            return -1
        else:
            return len(b)-b.find('1')

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends