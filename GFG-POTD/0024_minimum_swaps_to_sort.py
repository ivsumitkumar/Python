'''
LEVEL:>>> Medium
Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.


Example 1:

Input:
nums = {2, 8, 5, 4}
Output:
1
Explaination:
swap 8 with 4.
Example 2:

Input:
nums = {10, 19, 6, 3, 5}
Output:
2
Explaination:
swap 10 with 3 and swap 19 with 5.

Your Task:
You do not need to read input or print anything. Your task is to complete the function minSwaps() which takes the nums as input parameter and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 


Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)


Constraints:
1 ≤ n ≤ 105
1 ≤ numsi ≤ 106

Related Topics:>>>
Arrays
Graph
Sorting

SAMPLE INPUT:>>>
1
4
2 8 5 4
OUTPUT:>>> 1

SAMPLE INPUT:>>>
1
10
2 6 4 8 9 3 5 7 0 1
OUTPUT:>>> 8
'''
class Solution:
   def fn(self,a):
       return a[1]
   
   #Function to find the minimum number of swaps required to sort the array.
   def minSwaps(self, a):
       n = len(a)
       r = range(n)
       awithindex = [(i, a[i]) for i in r]  # 0 is index, 1 is value
       #print("original ", awithindex)
       awithindex.sort(key=self.fn)  # sort with value
       #print("sorted", awithindex)
       count = 0

       i = 0

       while i <= n - 1:
           if awithindex[i][0] == i:
               i += 1  # element in proper index
               continue
           index = awithindex[i][0]
           a[i], a[index] = a[index], a[i]
           #print("swap ", i, "with ", index, " values ", a[i], " with ", a[index])
           #print(a)
           awithindex[i], awithindex[index] = awithindex[index], awithindex[i]
           # self.swap( i, awithindex[i][0])
           #print(awithindex)
           count += 1

       return count

#{ 
#  Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)

# } Driver Code Ends