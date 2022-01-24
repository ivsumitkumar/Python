'''
Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

Example 1:

Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explaination: The next permutation of the 
given array is {1, 2, 4, 3, 5, 6}.
Example 2:

Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explaination: As arr[] is the last 
permutation. So, the next permutation 
is the lowest one.
Your Task:
You do not need to read input or print anything. Your task is to complete the function nextPermutation() which takes N and arr[ ] as input parameters and returns a list of numbers containing the next permutation.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10000

Related Topics:>>
 Permutation
 Constructive algo
 Arrays

SAMPLE INPUT:>>
1
6
1 2 3 6 5 4
OUTPUT:>> 1 2 4 3 5 6

SAMPLE INPUT:>>
1
3
3 2 1
OUTPUT:>> 1 2 3
'''
#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        if(N==1):
           return arr
        i  = N-2
        j = N-1
        while(i >= 0 and arr[i] > arr[i+1]):
            i -= 1
        if(i == -1):
            return arr[::-1]
        while(j >= 0 and arr[j]<arr[i]):
            j -= 1
        arr[i],arr[j] = arr[j],arr[i]
        arr[i+1:] = reversed(arr[i+1:])
      
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends