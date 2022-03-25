'''
LEVEL:>>> EASY
Given an array A of N length. We need to calculate the next greater element for each element in a given array. If the next greater element is not available in a given array then we need to fill -10000000 at that index place.

Example 1:

Input : arr[] = {13, 6, 7, 12}
Output : _ 7 12 13 
Explanation:
Here, at index 0, 13 is the greatest value 
in given array and no other array element 
is greater from 13. So at index 0 we fill 
'-10000000'.

Example 2:

Input : arr[] = {6, 3, 9, 8, 10, 2, 1, 15, 7} 
Output :  7 6 10 9 15 3 2 _ 8
Explanation: Here, at index 7, 15 is the greatest
value in given array and no other array element is
greater from 15. So at index 7 we fill '-10000000'.
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function greaterElement() that takes an array (arr), sizeOfArray (n), and return an array that displays the next greater element to element at that index. The driver code takes care of the printing.

Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(N).

 

Constraints:
1 ≤ N ≤ 105
-106 ≤ Ai ≤ 106

Related Topics:>>>
Arrays
CPP
Searching
Sorting
STL

SAMPLE INPUT:>>>
1
4
13 6 7 12

OUTPUT:>>>
_ 7 12 13 
'''
#User function Template for python3


def greaterElement (arr,  n) : 
   #Complete the function
   s=list(set(arr))
   s= sorted(s)
   
   temp_dict= {s[i]:i for i in range(len(s))}
   
   for i in range(n):
       ind = temp_dict[arr[i]]
       
       if ind+1==len(s):
           arr[i]=-10000000
       else:
           arr[i]=s[ind+1]
   return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = greaterElement(arr, n);
    ans = ""
    for i in res:
        if(i == -10000000):
            ans += "_ "
        else:
            ans += str(i)+" "
    print(ans)



# } Driver Code Ends