'''
LEVEL:>>> Hard
Given an array numbers[] of N positive integers and a positive integer X, The task is to find the number of ways that X can be obtained by writing pair of integers in the array numbers[] next to each other. In other words, find the number of ordered pairs (i,j) such that i != j and X is the concatenation of numbers[i] and numbers[j]

Example 1:

Input:
N = 4 
numbers[] = {1, 212, 12, 12}
X = 1212
Output:
3
Explanation:
We can obtain X=1212 by concatenating:
numbers[0] = 1 with numbers[1] = 212
numbers[2] = 12 with numbers[3] = 12
numbers[3] = 12 with numbers[2] = 12
Example 2:

Input: 
N = 3
numbers[] = {11, 11, 110}
X = 11011
Output:
2
Explanation:
We can obtain X=11011 by concatenating:
numbers[2] = 110 with numbers[0] = 11
numbers[2] = 110 with numbers[1] = 11
Your Task:
You dont need to read input or print anything. Your task is to complete the function countPairs() which takes the integer N , the integer X, and the array numbers[] as the input parameters, and returns the number of pairs which satisfies the above condition.

Expected Time Complexity: O(N*Log10(A[i]) + (Log10X)2)
Expected Auxiliary Space: O(N*Log10(A[i]))

Constraints:
1 ≤ N ≤ 5*104 
1 ≤ numbers[] ≤ 109
1 ≤ X ≤ 109

Related topics:>>>
Map 
Data Structures

SAMPLE INPUT:>>>
14 1212
1 212 12 12
OUTPUT:>> 3
'''
#User function Template for python3
class Solution:
    
    def countPairs(self, N, X, numbers): 
       #code here
       l = len(str(X))
       s_x = str(X)

       #Step 1
       dic = {(0,i):0 for i in range(l-1)}
       for i in range(1, l):
           dic[(i,l-1)] = 0

        #step 2
       for num in numbers:
           s_num = str(num)
           if len(s_num) >= l:
               continue
           if s_x[:len(s_num)] == s_num:
               dic[(0,len(s_num)-1)] += 1
           if s_x[l-len(s_num):] == s_num:
               dic[(l-len(s_num),l-1)] += 1
       count = 0

        #step 3
       for i in range(0, l-1):
           if l%2 == 0 and (l//2)-1 == i:
               if s_x[:i+1] == s_x[i+1:]:
                   count += (dic[(0,i)] * (dic[(i+1, l-1)]-1))
               else:
                   count += (dic[(0,i)] * dic[(i+1, l-1)])
           else:
               count += (dic[(0,i)] * dic[(i+1, l-1)])
       return count


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)


# } Driver Code Ends