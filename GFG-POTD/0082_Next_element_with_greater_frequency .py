'''
LEVEL:>>> Medium
Given an array arr[ ] of n integers, for every element, find the closest element on it's right that has a greater frequency than its own frequency.

Frequency is the number of times the element appears in the array.

 

Example 1:

Input:
n = 6
arr[] = {2 1 1 3 2 1}
Output:
1 -1 -1 2 1 -1 
Explanation:
1 appears 3 times.
2 appears 2 times.
3 appears 1 time. 

For arr[0] ie, 2
arr[1] ie 1 is the closest element on its 
right which has greater frequency than the 
frequency of 2. For the arr[1] and arr[2] no element 
on the right has greater frequency than 1, 
so -1 will be printed. and so on. 
Example 2:

Input:
n = 10
arr[] = {5 1 2 3 2 5 5 4 5 2}
Output:
-1 2 5 2 5 -1 -1 5 -1 -1
 

Your task:
Your task is to complete the function print_next_greater_freq() which take two parameters arr and n.This function returns answer(as a list of integers) as explained above.


Expected time complexity: O(n)
Expected space complexity: O(n)


Constraints:
1 <= n <= 10^4
1 <= arr[i] <= 10^4

Related Topics:>>>
Hash
Stack

SAMPLE INPUT:>>>
1
10
5 1 2 3 2 5 5 4 5 2

OUTPUT:>>>
-1 2 5 2 5 -1 -1 5 -1 -1
'''
import collections

class Solution:
    def print_next_greater_freq(self,arr,n):
        res = [-1]*n
        mapp = collections.Counter(arr)
        temp = []
        
        
        for idx, val in enumerate(arr):
            if not temp:
                temp.append(idx)
            else:
                curr = mapp[val]
                while temp:
                    prev_idx = temp[-1]
                    prev_freq = mapp[arr[prev_idx]]
                    if prev_freq < curr:
                        res[prev_idx] = val
                        temp = temp[:len(temp)-1]
                    else:
                        break
                
                temp.append(idx)
                
        return res


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends