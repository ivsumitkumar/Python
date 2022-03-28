'''
LEVEL:>>> EASY
Given a number X and two positions (from right side) in binary representation of x, write a program that swaps N bits at given two positions and returns the result.

 

Example 1:

Input:
X = 47
P1 = 1
P2 = 5
N = 3
Output: 227
Explanation:
The 3 bits starting from the second bit 
(from the right side) are swapped with 3 bits
starting from 6th position (from the right side) 
X = 47 (00101111)
[001]0[111]1
ANS = [111]0[001]1
ANS = 227 (11100011)
Hence, the result is 227.  
 

Example 2:

Input:
X = 28
P1 = 0
P2 = 3
N = 2
Output: 7

Your Task:  
You don't need to read input or print anything. Your task is to complete the function swapBits() which takes the integer X, integer P1, integer P2, and integer N as input parameters and returns the new integer after swapping. 

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 


Constraints:
1 ≤ X ≤ 200
0 ≤ P1 < P2 ≤ 11
1 ≤ N ≤ 5

Related Topics:>>> Bit Magic

SAMPLE INPUT:>>>
1
47
1
5

OUTPUT:>>>
227
'''
#User function Template for python3

class Solution:
    def swapBits(self, X, P1, P2, N):
        m=(1<<(N-1)) | ((1<<(N-1))-1)
        bs1, bs2=m&(X>>P1), m&(X>>P2)
        X&=~((m<<P1)|(m<<P2))
        X= X | (bs1<<P2) | (bs2<<P1)
        return X
         



#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends