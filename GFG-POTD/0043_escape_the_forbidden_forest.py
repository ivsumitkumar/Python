'''
Level:>>> Medium
Penelope and her classmates are lost in the Forbidden Forest and the Devil is out to get them. But Penelope has magical powers that can build bridges across the dangerous river and take her friends to safety. The only bridges that can withstand the Devil's wrath are the ones built between two similar trees in the forest. 
Given str1 and str2 denoting the order of trees on either side of the river, find the maximum number of bridges that Penelope can build and save everyone from the Devil. 
Note: Each tree in the forest belongs to one of the 3 categories represented by * or # or @

Example 1:

Input:
str1 = "*@#*" 
str2 = "*#"
Output:
2
Explanation:
str1 = "*@#*" and str2 = "*#" 
Two bridges can be built between the banks 
of the river in the following manner. 
* @ # *
|      |
*     #
Example 2:

Input:
str1 = "***"
str2 = "##"
Output:
0
Your Task:
You don't need to read input or print anything. Complete the function build_bridges() that takes str1 and str2 as input parameters and returns the maximum number of bridges that can be built. 

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)

Constraints:
1 ≤ N, M ≤ 100
Where, N and M are the size of the string str1 and str2 respectively.

Related Topics:>>>
Strings
LCS
Dynamic Programming

SAMPLE INPUT:>>>
1
**#*#@##@@ **#*#@
OUTPUT:>>> 6

SAMPLE INPUT:>>>
1
*@#* *#
OUTPUT:>>> 2
'''
class Solution:
   def build_bridges(self, text1, text2):
       # code here
       matrix = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
       for i in range(len(text1)-1,-1,-1):
           for j in range(len(text2)-1,-1,-1):
               if text1[i] == text2[j]:
                   matrix[i][j] = 1 + matrix[i+1][j+1]
               else:
                   matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])
       return matrix[0][0]


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        obj = Solution()
        str1, str2 = input().split()
        print(obj.build_bridges(str1, str2))

# } Driver Code Ends