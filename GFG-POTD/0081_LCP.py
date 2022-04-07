'''
LEVEL:>>> Medium
Geek is at the geek summer carnival. He is given an array of N strings. To unlock exclusive course discounts he needs to find the longest common prefix among all strings present in the array. Can you help him ?


Example 1:

Input:
N = 4
ar[] = {geeksforgeeks, geeks, geek, geezer}

Output:
gee

Explanation: 
Longest common prefix in all the given string is gee. 
 

Example 2:

Input:
N = 3
ar[] = {apple, ape, april}

Output:
ap

Your Task:
You don't need to read input or print anything. Complete the function LCP() that takes integer n and ar[] as input parameters and return the LCP (in case there is no common prefix return -1). 

 

Expected time complexity: O(NlogN)
Expected space complexity: O(string length)


Constraints:
1 <= N <= 10^3
1 <= String Length <= 100

Related Topics:>>>
Searching
sorting

SAMPLE INPUT:>>>
1
4
geeksforgeeks geeks geek geezer

OUTPUT:>>>
gee
'''
#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        #code here
        smallest = arr[0]
        for word in arr:
            
            while not word.startswith(smallest) and smallest:
                smallest=smallest[:-1]
            if not smallest:
                return -1
     
        return smallest

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends