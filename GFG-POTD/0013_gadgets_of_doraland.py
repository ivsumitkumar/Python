'''
LEVEL:>> Easy
In Doraland, people have unique Identity Numbers called D-id. Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only. N customers visit his shop and D-id of each customer is given in an array array[ ]. In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id. Find the D-ids of people he sells his K gadgets to.

Example 1:

Input:
N = 6
array[] = {1, 1, 1, 2, 2, 3}
K = 2
Output: 
1 2
Explanation: 
Customers with D-id 1 and 2 are most 
frequent.
Example 2:

Input:
N = 8
array[] = {1, 1, 2, 2, 3, 3, 3, 4}
K = 2
Output: 
3 2
Explanation: People with D-id 1 and 2 have 
visited shop 2 times Therefore, in this 
case, the answer includes the D-id 2 as 2 > 1.
Your Task:
You don't need to read input or print anything. Complete the function TopK() which takes array[ ] and integer K as input parameters and returns an array containing D-id of customers he has decided to sell his gadgets to.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
1 ≤ D-id ≤ 104

Related Topics:>>
 Hash
 Heap

 SAMPLE INPUT:>>
1
6
1 1 1 2 2 3
2
 OUTPUT:>> 1 2

SAMPLE INPUT:>>
1
8
1 1 2 2 3 3 3 4
2
 OUTPUT:>> 3 2
 '''
 #User function Template for python3

class Solution:
    def TopK(self, array, k):
        # code here
        d=dict()
        for i in array:
            d[i]=d[i]+1 if d.get(i) else 1
        res=sorted(d,key=lambda k:(d[k],k),reverse=True)
        return res[:k]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        res = obj.TopK(array, k)
        for each in res:
            print(each, end=' ')
        print()

# } Driver Code Ends