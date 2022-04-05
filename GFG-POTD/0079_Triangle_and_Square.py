'''
Level:>>> EASY
Geek has a ticket to the Geek Summer Carnival. The ticket has a positive integer B written on it. B denotes the base of a right-angled isosceles triangle. 
Geek can avail discounts on X courses in the carnival.

X is the maximum number of squares of size 2x2 units that can fit in the given right-angled isosceles triangle. 
Find X. 


Example 1:

Input:
B = 8
Output:
6 
Explanation: 


Example 2:

Input:
B = 2
Output:
0

Your Task:
You don't need to read input or print anything. Complete the function countSquare() that takes integer b as input parameter and returns the number of possible squares that can fit into the isosceles triangle. 


Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= B <= 1000

Related topics:>>>
Mathematical
Geometric

SAMPLE INPUT:>>>
1
8
OUTPUT:>>> 6
'''
#User function Template for python3

class Solution:
    def countShare(self,B):
        #code here
        b=B//2
        return int(b*(b-1)/2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        b=int(input().strip())
        obj=Solution()
        print(obj.countShare(b))
        
# } Driver Code Ends