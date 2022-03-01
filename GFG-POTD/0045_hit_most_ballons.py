'''
Level:>>> Medium
You are given an infinite two-dimensional grid. There are N balloons placed at certain coordinates of the grid. You have an arrow with yourself, which you will be using to shoot the balloons. You can select any point on the grid as your starting point and any point on the grid as the target point. When you fire the arrow, all ballons lying on the shortest path between the starting point and target point will be burst. Given the coordinates of the N ballons in an array arr, your task is to find out the maximum number of balloons that you can fire in one arrow shot.

Example 1:

Input:
N = 3
arr[] = {{1, 2}, {2, 3}, {3, 4}}
Output:
3
Explanation:
If you position yourself at point (1,2)
and fire the arrow aiming at the point (3,4).
Then all the balloons will burst.
Example 2:

Input: 
N = 3
arr[] = {{2,2}, {0,0}, {1,2}} 
Output:
2
Explanation: 
If you position yourself at point (2,2)
and fire the arrow aiming at the point (0,0).
Then the two balloons present at the two points
will burst.
Your Task:
Complete the function mostBalloons() which takes the integers N and the array arr as the input parameters, and returns the maximum number of balloons that can be burst using one arrow.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 103
-109 ≤ arr[i][j] ≤ 109

Related Topics:>>>
Mathematics
Geomatry

SAMPLE INPUT:>>>
3
1 2 3
2 3 4
OUTPUT:>>> 3
'''
#User function Template for python3

class Solution: 
    def mostBalloons(self, N, arr):
        # Code here
        ans = 1
        for i in range(N):
            count = dict()
            same_pos=0
            for j in range(N):
                x_diff=arr[j][0]-arr[i][0]
                y_diff=arr[j][1]-arr[i][1]
                if x_diff == 0 and y_diff==0:
                    same_pos+=1
                else:
                    slope=float("inf") if y_diff==0 else x_diff/y_diff
                    count[slope]=count.get(slope,0)+1
            ans = max(ans,max(count.values()) + same_pos)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends
