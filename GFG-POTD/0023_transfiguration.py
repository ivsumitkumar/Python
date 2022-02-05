'''
LEVEL:>>> EASY
Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. 
Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.

Example 1:

Input: 
A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
Output: 3
Explanation:The conversion can take place 
in 3 operations:
1. Pick 'R' and place it at the front, 
   A="RGEEKSFOGEEKS"
2. Pick 'O' and place it at the front, 
   A="ORGEEKSFGEEKS"
3. Pick 'F' and place it at the front, 
   A="FORGEEKSGEEKS"
Example 2:

Input: 
A = "ABC" 
B = "BCA"
Output: 2
Explanation: The conversion can take place 
in 2 operations:
1. Pick 'C' and place it at the front, 
   A = "CAB"
2. Pick 'B' and place it at the front, 
   A = "BCA"
Your Task:  
You don't need to read input or print anything. Complete the function transfigure() which takes strings A and B as input parameters and returns the minimum number of spells needed. If it is not possible to convert A to B then return -1.

Expected Time Complexity: O(max(|A|, |B|))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |A|, |B| ≤ 105
A and B consists of lowercase and uppercase letters of english alphabet only.

Related Topics:>>>
String
Hash

SAMPLE INPUT:>>>
1
GEEKSFORGEEKS FORGEEKSGEEKS
OUTPUT:>>> 3

SAMPLE INPUT:>>>
1
ABC BCA
OUTPUT:>>>2
'''
#User function Template for python3

from collections import defaultdict
class Solution:
    def transfigure(self, A, B):
        ALen = len(A)
        BLen = len(B)
        if ALen != BLen:
            return -1
        hashMap = defaultdict(int)
        for i in range(ALen):
            hashMap[ord(A[i])-ord('A')] += 1
            hashMap[ord(B[i])-ord('A')] -= 1
        for key in hashMap:
            if hashMap[key]:
                return -1
        cnt = 0
        j = BLen-1
        for i in range(ALen)[::-1]:
            if A[i] == B[j]:
                j -= 1
            else:
                cnt += 1
        return cnt

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends