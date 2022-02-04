'''
LEVEL:>>> HARD

Given an array of words, find all shortest unique prefixes to represent each word in the given array. Assume that no word is prefix of another.

Example 1:

Input: 
N = 4
arr[] = {"zebra", "dog", "duck", "dove"}
Output: z dog du dov
Explanation: 
z => zebra 
dog => dog 
duck => du 
dove => dov 
Example 2:

Input: 
N = 3
arr[] =  {"geeksgeeks", "geeksquiz",
                       "geeksforgeeks"};
Output: geeksg geeksq geeksf
Explanation: 
geeksgeeks => geeksg 
geeksquiz => geeksq 
geeksforgeeks => geeksf
Your task:
You don't have to read input or print anything. Your task is to complete the function findPrefixes() which takes the array of strings and it's size N as input and returns a list of shortest unique prefix for each word
 
Expected Time Complexity: O(N*length of each word)
Expected Auxiliary Space: O(N*length of each word)
 
Constraints:
1 ≤ N, Length of each word ≤ 1000

Related Topics:>>> Trie

SAMPLE INPUT:>>>
1
4
zebra dog duck dove
OUTPUT:>>> z dog du dov

SAMPLE INPUT:>>>
1
3
geeksgeeks geeksquiz geeksforgeeks
OUTPUT:>>> geeksg geeksq geeksf
'''
#User function Template for python3

class Solution:
   def findPrefixes(self, arr, N):
       present=[]
       ans=[]
       for s in arr:
           prefix=s[0]
           while prefix in present:
               if prefix not in ans:
                   prefix=prefix+s[len(prefix)]
               else:
                   index=ans.index(prefix)
                   ans[index]=ans[index]+arr[index][len(ans[index])]
                   present.append(ans[index])
                   prefix=prefix+s[len(prefix)]
           ans.append(prefix)
           present.append(str(prefix))
       return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends