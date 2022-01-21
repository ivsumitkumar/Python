'''
Given a Binary Number B, find its decimal equivalent.
 

Example 1:

Input: B = 10001000
Output: 136
Example 2:

Input: B = 101100
Output: 44
 

Your Task:
You don't need to read or print anything. Your task is to complete the function binary_to_decimal() which takes the binary number as string input parameter and returns its decimal equivalent.
 

Expected Time Complexity: O(K * Log(K)) where K is number of bits in binary number.
Expected Space Complexity: O(1)
 

Constraints:
1 <= number of bits in binary number  <= 16

SAMPLE INPUT:>> 10001000
OUTPUT:>> 136

SAMPLE INPUT:>> 101100
OUTPUT:>> 44

'''
class Solution:
    def binary_to_decimal(self, str):
        # Code here
        return int(str,2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution();
        ans = ob.binary_to_decimal(str)
        print(ans)
# } Driver Code Ends
