'''Given two binary max heaps as arrays, merge the given heaps to form a new max heap.

 

Example 1:

Input  : 
n = 4 m = 3
a[] = {10, 5, 6, 2}, 
b[] = {12, 7, 9}
Output : 
{12, 10, 9, 2, 5, 7, 6}
Explanation :
           10
         /    \
        5      6
      /  
     2
           12
         /    \
        7      9


           12
         /    \
        10     9
      /   \   / \  
     2     5 7   6



Your Task:  
You don't need to read input or print anything. Your task is to complete the function mergeHeaps() which takes the array a[], b[], its size n and m, as inputs and return the merged max heap. Since there can be multiple solutions, therefore, to check for the correctness of your solution, your answer will be checked by the driver code and will return 1 if it is correct, else it returns 0.

Expected Time Complexity: O(n.Logn)
Expected Auxiliary Space: O(n + m)

Constraints:
1 <= n, m <= 105
1 <= a[i], b[i] <= 2*105

INPUT:>>
1
4 3
10 5 6 2
12 7 9
OUTPUT:>>
1
'''
#User function Template for python3

class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        self.a=a
        self.b=b
        self.n=n
        self.m=m
        ab=self.a + self.b
        mn=self.n + self.m
        Solution.maxheap(ab,mn)
        return ab
        
    def maxheap(k,mn):
        for i in range((mn//2)-1,-1,-1):
            Solution.heapify(k,mn,i)
    
    def heapify(k,mn,indx):
        if indx >= mn:
            return
        left=(2*indx)+1
        right=(2*indx)+2
        mx=0
        if left < mn and k[left]>k[indx]:
            mx=left
        else:
            mx=indx
        if right < mn and k[right]>k[mx]:
            mx=right
            
        if mx != indx:
            k[mx],k[indx] = k[indx],k[mx]
            Solution.heapify(k,mn,mx)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def isMerged(arr1, arr2, merged):
    if (len(arr1) + len(arr2) != len(merged)):
        return False
    arr1 += arr2
    arr1.sort()
    mergedCopy = sorted(merged)
    if (arr1 != mergedCopy):
        return False
    for i in range(1, len(merged)):
        if merged[i] > merged[(i-1)//2]:
            return False

    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        copyA = a[:]
        copyB = b[:]
        obj = Solution()
        merged = obj.mergeHeaps(a, b, n, m)
        flag = isMerged(copyA, copyB, merged)
        print(0 if flag == False else 1)

# } Driver Code Ends