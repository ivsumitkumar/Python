'''
LEVEL:>>> Medium
Given an array of size N containing positive integers n and a number k,The absolute difference between values at indices i and j is |a[i] – a[j]|. There are n*(n-1)/2 such pairs and you have to print the kth smallest absolute difference among all these pairs.
 

Example 1:

Input : 
N = 4
A[] = {1, 2, 3, 4}
k = 3
Output : 
1 
Explanation :
The possible absolute differences are :
{1, 2, 3, 1, 2, 1}.
The 3rd smallest value among these is 1.
 
Example 2:
Input : 
N = 2
A[] = {10, 10}
k = 1
Output :
0

Your Task:  
You don't need to read input or print anything. Your task is to complete the function kthDiff() which takes the array A[], its size N and an integer k as inputs and returns the kth smallest absolute difference among all these pairs.

 

Expected Time Complexity: O( N. (Log(N))2 )
Expected Auxiliary Space: O(Log(N))

 

Constraints:
1<=N<=105
1<=a[i]<=105
1 <= k <= n*(n-1)/2

Related Topics:>>>
Arrays

SAMPLE INPUT:>>>
1
4
1 2 3 4
3
OUTPUT:>>> 1

SAMPLE INPUT:>>>
1
2
10 10
1
OUTPUT:>>> 0
'''
#User function Template for python3

def sub(l):
    return abs(l[0]-l[1])
    
def kthDiff( a, n, k):
    dif=[]
    for i in range(n):
        for j in range(i+1,n):
            dif.append(sub([a[i],a[j]]))
            
    dif.sort()
    # print(l)
    return dif[k-1]   
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(kthDiff(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends