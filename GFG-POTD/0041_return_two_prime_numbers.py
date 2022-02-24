'''
Level:>>> Hard
Given an even number N (greater than 2), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only the pair whose minimum value is the smallest among all the minimum values of pairs and print the minimum element first.

NOTE: A solution will always exist, read Goldbachs conjecture(https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) 

Example 1:

Input: N = 74
Output: 3 71
Explaination: There are several possibilities 
like 37 37. But the minimum value of this pair 
is 3 which is smallest among all possible 
minimum values of all the pairs.
Example 2:

Input: 4
Output: 2 2
Explaination: This is the only possible 
prtitioning of 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function primeDivision() which takes N as input parameter and returns the partition satisfying the condition.

Expected Time Complexity: O(N*log(logN))
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 104 

Related Topics:>>>
Mathematical

SAMPLE INPUT:>>>
1
74
OUTPUT:>>>
3 71
SAMPLE INPUT:>>>
1
500
OUTPUT:>>>
3 487
'''
#User function Template for python3

class Solution:
    def isPrime(self,n):#Function to check if number is prime
        limit = int(n ** 0.5)#If no cannot be divided till square root it is prime
        for i in range(2, limit + 1):
            if n % i == 0:
                return False#If remainder is 0 return False. Not prime
        return True
    def primeDivision(self, n):
        for i in range(2, n+1 ):
            if self.isPrime(i) and self.isPrime(n-i):#i and n-i will add up to n
                return [i,n-i]
        return [1,2]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends