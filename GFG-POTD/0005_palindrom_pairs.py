'''
Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.


Example 1:

Input:
N = 6
arr[] = {"geekf", "geeks", "or","keeg", "abc", 
          "bc"}
Output: 1 
Explanation: There is a pair "geekf"
and "keeg".
Example 2:

Input:
N = 5
arr[] = {"abc", "xyxcba", "geekst", "or", "bc"}
Output: 1
Explanation: There is a pair "abc"
and "xyxcba".

Your Task:  
You don't need to read input or print anything. Your task is to complete the function palindromepair() which takes the array arr[], its size N and returns true if palindrome pair exists and returns false otherwise.
The driver code itself prints 1 if returned value is true and prints 0 if returned value is false.
 

Expected Time Complexity: O(N*l2) where l = length of longest string in arr[]
Expected Auxiliary Space: O(N*l2) where l = length of longest string in arr[]
 

Constraints:
1 ≤ N ≤ 104
1 ≤ |arr[i]| ≤ 10

Related Topics:>> Trie

SAMPLE INPUT 01:>>
1
6
geekf
geeks
or
keeg
abc
bc
OUTPUT:>> 1

SAMPLE INPUT 02:>>
1
5
abc
xyxcba
geekst
or
bc
OUTPUT:>> 
1
'''

#User function Template for python3

class Solution:
    def palindromepair(self, N, arr):
        # code here 
        for i in range(N):
            for j in range(i+1,N):
                if arr[i]+arr[j] == (arr[i]+arr[j])[::-1]:
                    return 1
                if arr[j]+arr[i] == (arr[j]+arr[i])[::-1]:
                    return 1
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        for i in range(N):
            s = input()
            arr.append(s)
        
        ob = Solution()
        print(ob.palindromepair(N,arr))
# } Driver Code Ends