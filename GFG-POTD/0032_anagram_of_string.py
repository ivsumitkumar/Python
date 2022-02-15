'''
LEVEL:>>> Easy
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
Example 2:

Input:
S1 = cddgk
S2 = gcd
Output: 2
Explanation: We need to remove d and
k from S1.
Your Task:
Complete the function remAnagram() which takes two strings S1, S2 as input parameter, and returns minimum characters needs to be deleted.

Expected Time Complexity: O(max(|S1|, |S2|)), where |S| = length of string S.
Expected Auxiliary Space: O(26)

Constraints:
1 <= |S1|, |S2| <= 105

Related Topics:>>>
Anagram
Strings

SAMPLE INPUT:>>>
1
bcadeh
hea
OUTPUT:>>> 3
'''
# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
   j = 0
   t = len(str1)+len(str2)
   for i in str1 :
       j += min(str1.count(i),str2.count(i))
       str1=str1.replace(i,"")
       str2=str2.replace(i,"")
       
   return (t -2*j)
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends