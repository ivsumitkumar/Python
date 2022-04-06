'''
LEVEL:>>> Medium

Geek wants to select the maximum number of course bundles at the Geek Summer Carnival.
You are given a finite number of courses and N range of numbers each depicting a bundle of courses. Select the maximum number of bundles such that no courses overlap in any of the bundle.

Note: The ending of a range being the same as start of another isn't considered as an overlap.


Example 1:

Input:
N = 4
Bundles = 
1 5
2 3
1 8
3 5

Output:
2

Explanation: 

We can select 2 bundles at max while 
staying true to the condition. For this, 
we can pick the ranges (2,3) and (3,5) 
without any overlap. 
 

Example 2:

Input:
N = 5
Bundles = 
7 9 
2 8 
1 3 
10 11 
10 16

Output:
3

Explanation: 

We can pick the ranges (1,3), 
(7,9) and (10,11) without any overlap.

Your Task:
You don't need to read input or print anything. Complete the function max_non_overlapping() that takes a 2D array representing N ranges as input parameter.  Return the maximum number of course bundles. 


Expected time complexity: O(NlogN)
Expected space complexity: O(1)


Constraints:
1 <= N <= 1000
0 <= range[i][j] <= 1000

Related Topics:>>>
Sorting

SAMPLE INPUT:>>>
1
4
1 5 2 3 1 8 3 5

OUTPUT:>>>
2
'''
# ranges[i][0] is the start of ith range
# ranges[i][1] is the end of ith range

class Solution:
        
    def max_non_overlapping(self,ranges):
        # code here
        # sort acc. the second value
        ranges.sort(key = lambda x :x[1])
        prev = -1
        count = 0
        for i in range(n):
            if ranges[i][0] >= prev:
                count+=1
                prev = ranges[i][1]
        return count

#{ 
#  Driver Code Starts
# driver code
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        ranges = [[]  for j in range(n)]
        j=0
        for i in range(0,2*n,2):
            ranges[j].append(int(line[i]))
            ranges[j].append(int(line[i+1]))
            j+=1
            
        obj=Solution()
        print( obj.max_non_overlapping(ranges) )
# } Driver Code Ends