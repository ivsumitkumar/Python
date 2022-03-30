'''
LEVEL:>>> EASY
Given an array A[] of size N. Find the number of pairs (i, j) such that
Ai XOR Aj = 0, and 1 ≤ i < j ≤ N.

Example 1:

â€‹Input : arr[ ] = {1, 3, 4, 1, 4}
Output : 2
Explanation:
Index( 0, 3 ) and (2 , 4 ) are only pairs 
whose xors is zero so count is 2.

â€‹Example 2:

Input : arr[ ] = {2, 2, 2} 
Output :  3

 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function calculate() that takes an array (arr), sizeOfArray (n), and return the count of Zeros Xor's Pairs. The driver code takes care of the printing.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(1).



Output:
For each test case, output a single integer i.e counts of Zeros Xors Pairs

Constraints
2 ≤ N ≤ 10^5
1 ≤ A[i] ≤ 10^5

Related Topics:>>>
Arrays
Bit Magic
Sorting

SAMPLE INPUT:>>>
1
5
1 3 4 1 4
OUTPUT:>>>
2
'''
#User function Template for python3


def calculate (arr, n) : 
    #Complete the function
    p=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                p += 1
    return p


#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)


# } Driver Code Ends