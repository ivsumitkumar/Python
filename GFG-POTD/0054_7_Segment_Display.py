'''
Lvele:>>> Medium
Using seven segment display, you can write down any digit from 0 to 9 using at most seven segments. Given a positive number N and then a string S representing a number of N digits. You have to rearrange the segments in this N digit number to get the smallest possible N digit number. This number can have leading zeros. You can not waste any segment or add any segment from your own. You have to use all of the segments of the given N digits.

Note: You can refer this diagram for more details



Example 1:

Input:
N = 6
S = "234567"
Output:
000011
Explanation:
234567 has a total of 28 segments and
we can rearrange them to form 000011
which has 28 segments too. 000011 is the
smallest possible number which can be
formed on rearrangement.
Example 2:

Input:
N = 3
S = "011"
Output:
011
Explanation:
011 has a total of 10 segments and this
is the smallest number with 10 segments.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function sevenSegments() which takes an Integer N and a String S of length N as input and returns the smallest possible N digit number which can be made using all of the segments given.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 104

Related Topics:>>>
Greedy
Mathematical

SAMPLE INPUT:>>>
1
6
234567
OUTPUT:>>> 000011
'''
#User function Template for python3

class Solution:
    def sevenSegments(self, S, N):
        # code here
        hmap = {}
        hmap[0] = 6
        hmap[1] = 2
        hmap[2] = 5
        hmap[3] = 5
        hmap[4] = 4
        hmap[5] = 5
        hmap[6] = 6
        hmap[7] = 3
        hmap[8] = 7
        hmap[9] = 5
        seg = 0
        for i in S:
            seg += hmap[int(i)]
        #print(seg)
        ans = []
        for i in range(N):
            ans .append ('1')
            seg-=2
        for j in range(N):
            if seg == 4:
                ans[j] = '0'
                break
            elif seg > 4:
                ans[j] = '0'
                seg-=4
            elif seg < 4:
                if seg == 3:
                    ans[-1] = '2'
                elif seg == 2:
                    ans[-1] = '4'
                elif seg == 1:
                    ans[-1] = '7'
                
        if seg > 0 :
            k= N-1
            while(seg and k >= 0):
                last = hmap[int(ans[k])]
                newseg = last+1
                if str(newseg) == '7':
                    ans[k] = '8'
                seg-=1
                N-=1
        ans = "".join(ans)
        return ans 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.sevenSegments(S,N))
# } Driver Code Ends