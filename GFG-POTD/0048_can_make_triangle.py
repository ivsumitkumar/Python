'''
LEVEL:>>> Medium
Given an array A[] of N elements, You'd like to know how many triangles can be formed with side lengths equal to adjacent elements from A[].

Construct an array of integers of length N - 2 where ith element is equal to 1 if it is possible to form a triangle with side lengths A[i], A[i+1], and A[i+2]. otherwise 0.

Note: A triangle can be formed with side lengths a, b and c if a+b>c and a+c>b and b+c>a.

Example 1:

Input:
N = 4
A[] = {1, 2, 2, 4}
Output:
1 0
Explanation:
output[0] = 1 because we can form a 
triangle with side lengths 1,2 and 2.
output[1] = 0 because 2+2<4 so, we cannot 
form a triangle with side lengths 2,2 and 4.
Example 2:

Input: 
N = 5
A[] = {2, 10, 2, 10, 2}
Output:
0 1 0
Explanation:
output[0] = 0 because 2+2<10 so, we cannot
form a triangle with side lengths 2, 10 and 2. 
output[1] = 1 we can form a triangle with 
side lengths 10,2 and 10. 
output[1] = 0 because 2+2<10 so, we can
form a triangle with side lengths 2, 10 and 2. 
Your Task:
You dont need to read input or print anything. Your task is to complete the function canMakeTriangle() which takes the array A and the integer N as the input parameters, and returns the array of answers.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
3 ≤ N ≤ 105 
1 ≤ arr[i] ≤ 109

Related Topics:>>>
Geomatric
Mathematical

SAMPLE INPUT:>>>
1
4 
1 2 2 4
OUTPUT:>>> 1 0

SAMPLE INPUT:>>>
1
6
2 3 5 6 8 9
OUTPUT:>>> 0 1 1 1
'''


#User function Template for python3
class Solution:
    def istri(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return 1
        else:
            return 0

    def canMakeTriangle(self, A, N):
        #code here
        t = []
        for i in range(0, N - 2):
            t.append(self.istri(A[i], A[i + 1], A[i + 2]))
        return t


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends