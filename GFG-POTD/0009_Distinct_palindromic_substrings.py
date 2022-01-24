'''
Given a string str of lowercase ASCII characters, Count the number of distinct continuous palindromic sub-strings which are present in the string str.

Example 1:

Input:
str = "abaaa"
Output:
5
Explanation : These are included in answer:
"a","aa","aaa","aba","b"
Example 2:

Input
str = "geek"
Output: 
4
Explanation : Below are 4 palindrome sub-strings
"e","ee","g","k"
Your Task:
You don't need to read input or print anything. Your task is to complete the function palindromeSubStrs() which takes the string str as input parameter and returns the total number of distinct continuous palindromic sub-strings in str.

Expected Time Complexity : O(N2logN)
Expected Auxilliary Space : O(N2)

Constraints:
1 ≤ N ≤ 2*103, where N is the length of the string str.

Related Topics:>>
Dynamic Programming
Palindrome
STL
Strings

Sample Input:>>
1
abaaa
OUTPUT:>> 5
'''

#User function Template for python3

class Solution:
    def palindromeSubStrs(self, Str):
        # code here
        palindromes = set()
        #Loop through each index
        for i in range(len(Str)):
           #find all odd length substring palindrome with s[i] as mid point
           self.find(Str,i,i,palindromes)
           
           #find all even length substring palindrome with s[i] and s[i+1] as mid point
           self.find(Str,i,i+1,palindromes)
       
        return len(palindromes)
           
   
    def find(self,Str,low,high,palindromes):
        while(low>=0 and high<=len(Str)-1 and Str[low]==Str[high]):
            #add palindrome to set
            palindromes.add(Str[low:high+1])
           
            #expand in both directions
            low = low-1
            high = high+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.palindromeSubStrs(Str))
# } Driver Code Ends
