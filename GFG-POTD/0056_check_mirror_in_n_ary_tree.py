'''
LEVEL:>>> Medium
Given two n-ary trees. Check if they are mirror images of each other or not. You are also given e denoting the number of edges in both trees, and two arrays, A[] and B[]. Each array has 2*e space separated values u,v denoting an edge from u to v for the both trees.


Example 1:

Input:
n = 3, e = 2
A[] = {1, 2, 1, 3}
B[] = {1, 3, 1, 2}
Output:
1
Explanation:
   1          1
 / \        /  \
2   3      3    2 
As we can clearly see, the second tree
is mirror image of the first.
Example 2:

Input:
n = 3, e = 2
A[] = {1, 2, 1, 3}
B[] = {1, 2, 1, 3}
Output:
0
Explanation:
   1          1
 / \        /  \
2   3      2    3 
As we can clearly see, the second tree
isn't mirror image of the first.

Your Task:
You don't need to read input or print anything. Your task is to complete the function checkMirrorTree() which takes 2 Integers n, and e;  and two arrays A[] and B[] of size 2*e as input and returns 1 if the trees are mirror images of each other and 0 if not.


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)


Constraints:
1 <= n,e <= 105

Related Topics:>>>
Queue
Stack
STL
Tree

SAMPLE INPUT:>>>
1
3 2
1 2 1 3
1 3 1 2
OUTPUT:>>> 1
'''
class Solution:
    def checkMirrorTree(self, n, e, A, B):
        dictA={}
        dictB={}
        for x in range(0,2*e,2):
            if A[x] in dictA:
                dictA[A[x]].append(A[x+1])
            else:
                dictA[A[x]]=[A[x+1]]
            if B[x] in dictB:
                dictB[B[x]].append(B[x+1])
            else:
                dictB[B[x]]=[B[x+1]]
        for x in dictA:
            if dictA[x]!=list(reversed(dictB[x])):
                return 0
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.checkMirrorTree(n,e,A,B))
# } Driver Code Ends