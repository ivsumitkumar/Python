'''
Level:>>> Medium
Given a non-negative number N in the form of string. The task is to apply at most one swap operation on the number N so that the result is just a previous possible number.

Note:  Leading zeros are not allowed.

 

Example 1:

Input :
S = "12435"
Output: 
12345
Explanation:
Although the number 12354 
will be the largest smaller 
number from 12435. But it is 
not possible to make it using 
only one swap. So swap 
4 and 3 and get 12345.
 

Example 2:

Input: 
S = " 12345"
Output: 
-1
Explanation:
Digits are in increasing order. 
So it is not possible to 
make a smaller number from it.
 

Your Task:

You don't need to read input or print anything. Your task is to complete the function previousNumber() which takes the string S and returns the previous number of S. If no such number exists return -1;

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
2<=|Number length |<=10^5

Related Topics:>>>
Strings
Numbers

SAMPLE INPUT:>>>
1
12435

OUTPUT:>>>
12345
'''
#User function Template for python3
class Solution:
    
    def previousNumber(ob,s):
        # code here 
        n= len(s)
        arr = list(s)
        flag = False
        for i in range(n-1):
            if arr[i] <= arr[i+1]:
                continue
            else:
                Flag = True
                break
        if flag:
            return -1
        idx = None
        for i in range(n-1,0,-1):
            if arr[i-1] > arr[i]:
                idx = i-1
                break
        if idx == None:
            return -1
        temp = '-999999'
        for j in range(n-1,idx,-1):
            if arr[j] < arr[idx]:
                if arr[j] >= temp:
                    idx2 = j
                    temp = arr[idx2]
        arr[idx],arr[idx2] = arr[idx2],arr[idx]
        ans = ''.join(arr)
        if ans[0] == '0':
            return -1
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.previousNumber(S))
# } Driver Code Ends