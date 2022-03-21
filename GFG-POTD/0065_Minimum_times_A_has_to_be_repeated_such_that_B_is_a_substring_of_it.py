'''
LEVEL:>>> Medium
Given two strings A and B. Find minimum number of times A has to be repeated such that B is a Substring of it. If B can never be a substring then return -1.

 

Example 1:

Input:
A = "abcd"
B = "cdabcdab"
Output:
3
Explanation:
Repeating A three times (“abcdabcdabcd”),
B is a substring of it. B is not a substring
of A when it is repeated less than 3 times.
Example 2:
Input:
A = "ab"
B = "cab"
Output :
-1
Explanation:
No matter how many times we repeat A, we can't
get a string such that B is a substring of it.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function minRepeats() which takes 2 strings A, and B respectively and returns the minimum number of times A has to be repeated such that B is a substring of it. Return -1 if it's not possible.


Expected Time Complexity: O(|A| * |B|)
Expected Auxiliary Space: O(|B|)


Constraints:
1 ≤ |A|, |B| ≤ 103
String A and B consists of lower case alphabets

Related Topics:>>> 
Strings
Pattern Searching
Searching

SAMPLE INPUT:>>>
1
abcd
cdabcdab

OUTPUT:>>>
3
'''
#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        for b in B:
            if b not in A:
                return -1
        tmp=''
        for i in range(1000):
            if B in tmp:
                return i
            tmp+=A
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends