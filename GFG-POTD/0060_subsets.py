'''
LEVEL:>>> Medium
Given a set of positive integers, find all its subsets.

Example 1 :

Input : 
array = {1, 2, 3}
Output :
// this space denotes null element. 
1
1 2
1 2 3
1 3
2
2 3
3
Explanation: 
The following are the subsets 
of the array {1, 2, 3}.
Example 2 :

Input :
array = {1, 2}
Output :

1 
1 2
2
Explanation :
The following are the 
subsets of {1, 2}.
Your task :
You don't have to read input or print anything. Your task is to complete the function subsets() which takes the array of integers as input and returns the list of list containing the subsets of the given set of numbers in lexicographical order.
 
Expected Time Complexity : O(2^n)))
Expected Auxiliary Space : O(2^n*length of each subset)
 
Constraints :
1 <= n <= 20
1 <= arr[i] <=10

Related Topics:>>>
BackTracking
Recursion

SAMPLE INPUT:>>>
1
3
1 2 3

OUTPUT:>>>
1 
1 2 
1 2 3 
1 3 
2 
2 3 
3
'''
#User function Template for python3

class Solution:
   def subsets(self, A):
       #code here
       res=[]
       
       subset=[]
       def bfs(i):
           if(i>=len(A)):
               res.append(subset.copy())
               return
           # include
           subset.append(A[i])
           bfs(i+1)
           # exc
           subset.pop()
           bfs(i+1)
           
       bfs(0)
       res.sort()
       return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends