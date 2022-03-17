'''
LEVEL:>>> Hard
Find the number of unique words consisting of lowercase alphabets only of length N that can be formed with at-most K contiguous vowels. 


Example 1:

Input:
N = 2
K = 0
Output:
441
Explanation:
Total of 441 unique words are possible
of length 2 that will have K( =0) vowels
together, e.g. "bc", "cd", "df", etc are
valid words while "ab" (with 1 vowel) is
not a valid word.

Example 2:

Input:
N = 1
K = 1
Output:
26
Explanation:
All the english alphabets including
vowels and consonants; as atmost K( =1)
vowel can be taken.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function kvowelwords() which takes an Integer N, an intege K and returns the total number of words of size N with atmost K vowels. As the answer maybe to large please return answer modulo 1000000007.


Expected Time Complexity: O(N*K)
Expected Auxiliary Space: O(N*K)


Constraints:
1 ≤ N ≤ 1000
0 ≤ K ≤ N

Related Topics:>>>
Dynamic Programming
Strings

SAMPLE INPUT:>>>
1
1 0
OUTPUT:>>> 21
'''
#User function Template for python3

class Solution:
    def kvowelwords(self, N,K):
        # code here
        large = 1000000007
        dp=[1]
        powers=[1]
        for _ in range(K):
            powers.append((powers[-1]*5)%large)
        for i in range(1,N+1):
            total=0
            for j in range(min(i+1,K+1)):
                count = powers[j]
                if i>j:
                    count = (count*21*dp[i-j-1])%large
                total = (total+count)%large
            dp.append(total)
        return dp[-1]




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N,K = map(int,input().split())
        ob = Solution()
        ans = ob.kvowelwords(N,K)
        print(ans)
# } Driver Code Ends