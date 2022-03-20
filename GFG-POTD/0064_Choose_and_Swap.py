'''
LEVEL:>>> EASY
You are given a string s of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.

Example 1:

Input:
A = "ccad"
Output: "aacd"
Explanation:
In ccad, we choose a and c and after 
doing the replacement operation once we get, 
aacd and this is the lexicographically
smallest string possible. 
 

Example 2:

Input:
A = "abba"
Output: "abba"
Explanation:
In abba, we can get baab after doing the 
replacement operation once for a and b 
but that is not lexicographically smaller 
than abba. So, the answer is abba. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function chooseandswap() which takes the string A as input parameters and returns the lexicographically smallest string that is possible after doing the operation at most once.

Expected Time Complexity: O(|A|) length of the string A
Expected Auxiliary Space: O(1)

 

Constraints:
1<= |A| <=105

Related Topics:>>>
Greedy

SAMPLE INPUT:>>>
1
ccad
OUTPUT:>>>
aacd
'''
#User function Template for python3


class Solution:
    def chooseandswap (self, A):
        # code here
       l = len(A)
       covered = set()
       for i in range(l):
           smaller = A[i]
           covered.add(smaller)
           for j in A[i+1:]:
               if j<smaller and j not in covered:
                   smaller = j
           if smaller != A[i]:
               break
       if smaller == A[i]:
           return A
       temp = A[i]
       res = ""
       for j in range(l):
           flag = True
           if temp == A[j]:
               flag = False
               res += smaller
           elif flag and A[j] == smaller:
               res += temp
           else:
               res+=A[j]
       return res




#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends