'''
Given n arrays of size m each. Find maximum sum obtained by selecting a number from each array such that the element selected from the i-th array is more than the element selected from (i-1)-th array. If maximum sum cannot be obtained then return 0.

Example 1:

â€‹Input : arr[ ] = {{1,7,4,3}, {4,2,5,1}, {9,5,1,8}}
Output : 18
Explanation:
We can select 4 from the first array,
5 from second array and 9 from the third array.

â€‹Example 2:

Input : arr[ ] = {{9,8,7}, {6,5,4}, {3,2,1}} 
Output :  0

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function maximumSum() that takes number of row N, a number of Column M, 2-d array (arr), and return the maximum sum if cannot be obtained then return 0. The driver code takes care of the printing.

Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N, M ≤ 500

Related Topics:>> Arrays, Greedy, Searching

SAMPLE INPUT:>>
1
3 3
9 8 7
6 5 4
3 2 1
OUTPUT:>> 0

SAMPLE INPUT:>>
1
3 4
1 7 4 3
4 2 5 1
9 5 1 8 
OUTPUT:>> 18

'''

#User function Template for python3

def maximumSum (n, m, arr) : 
    #Complete the function
    rev=arr[::-1]
    rsort= [sorted(i)[::-1] for i in rev]
    
    Max=rsort[0][0]
    elements=[]
    for i in range(1,n):
        for j in range(m):
            if Max > rsort[i][j]:
                elements.append(rsort[i][j])
                Max=rsort[i][j]
                break
        else:
            return 0
    else:
        return sum(elements)+rsort[0][0]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n, m = map(int , input().split())
    arr = []
    for i in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    ans = maximumSum(n, m, arr)
    print(ans)




# } Driver Code Ends
