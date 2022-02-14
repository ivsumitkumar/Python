'''
LEVEL:>>> Medium

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.
Example 2:

Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and 
smallest positive missing number is 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findTwoElement() which takes the array of integers arr and n as parameters and returns an array of integers of size 2 denoting the answer ( The first index contains B and second index contains A.)

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ N

Related Topics:>>>
Arrays

SAMPLE INPUT:>>>
1
2
2 2
OUTPUT:>>> 2 1

SAMPLE INPUT:>>>
1
23
2 21 17 16 22 3 9 10 14 12 20 11 6 4 8 7 23 15 18 13 1 10 19
OUTPUT:>>>
10 5
'''
#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        l=[]
        arrs=set(arr)
        l.append((sum(arr)-sum(arrs)))
        
        Max=max(arrs)
        result=int((Max*(Max+1))/2)-sum(arrs)
        if(result==0):
            l.append(Max+1)
        else:
            l.append(result)
        return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends