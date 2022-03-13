'''
LEVEL:>>> Medium
You are given a matrix having n rows and m columns. The special property of this matrix is that some of the cells of this matrix are blocked i.e. they cannot be reached. Now you have to start from the cell (1,1) and reach the end (n,m) provided during the journey you can move horizontally right from the current cell or vertically down from the current cell. Can you answer the number of ways you can traverse the matrix obeying the above constraints starting from (1,1) and ending at (n,m).
 

Example 1:

Input: n = 3, m = 3, k = 2,
blocked_cells = {{1,2},{3,2}}.
Output: 1
Explanation: There is only one path from
(1,1) to(3,3) which is (1,1)->(2,1)->(2,2)->
(2,3)->(3,3).
Example 2:

Input: n = 5, m = 5, k = 1,
blocked_cells = {{5,5}}
Output: 0
Explanation: There is no path to reach at 
(5,5) beacuse (5,5) is blocked.
 

Your Task:
You don't need to read or print anything, Your task is to complete the function FindWays() which takes n, m and blocked_cells as input parameter and returns total number of ways to reach at (n, m) modulo 109 + 7.
 

Expected Time Complexity: O(n*m)
Expected Space Complexity: O(n*m)
 

Constraints:
1 <= n, m <= 500
1 <= k <= n*m

Related Topics:>>>
Dynamic Programming

SAMPLE INPUT:>>>
1
3 3 2
1 2
3 2
OUTPUT:>>> 1
'''
#User function Template for python3

class Solution:
    def FindWays(self, n, m, b):
        d = {}
        for i in b:
            k = str(i[0])+','+str(i[1])
            d[k] = 0
        if str(n)+','+str(m) in d or str(1)+','+str(1) in d:
            return 0
        def r(n,m,mo={}):
           k = str(n) + ',' + str(m)
           if m == 1 and n == 1: return 1
           if m == 0 or n == 0: return 0
           if k in d : return 0
           if k in mo: return mo[k]
           mo[k] =  (r(n-1,m,mo)+r(n,m-1,mo)) % (10**9+7)
           return mo[k]
        return r(n,m,{})

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m, k= input().split()
        n = int(n); m = int(m); k = int(k);
        blocked_cells = []
        for i in range(k):
            a = list(map(int, input().split()))
            blocked_cells.append(a)
        obj = Solution()
        ans = obj.FindWays(n, m, blocked_cells)
        print(ans)

# } Driver Code Ends