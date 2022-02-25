'''
LEVEL:>>> Medium
There are two kinds of bots A and B in a 1-D array. A bot can only move left while B can only move right. There are also empty spaces in between represented by #. But its also given that the bots cannot cross over each other.

Given the initial state and final state, we should tell if the transformation is possible.

NOTE: There can be many bots of the same type in a particular array. 


Example 1:

Input:
s1 = #B#A#
s2 = ##BA#
Output: Yes
Explanation: Because we can reach the 
final state by moving 'B' to the 
right one step.

Example 2:

Input:
s1 = #B#A#
s2 = #A#B# 
Output: No
Explanation: Because the robots 
cannot cross each other.


Your Task:  
You don't need to read input or print anything. Your task is to complete the function moveRobots() which takes the initial and final states as strings s1 and s2 respectively and returns if a valid transformation can be done. Return "Yes" if possible, else "No".

 

Expected Time Complexity: O(|s1|)
Expected Auxiliary Space: O(|s1|)

 

Constraints:
1 <= |s1| = |s2| <= 105
The strings only consists of 'A', 'B' and '#'.

Related Topics:>>>
Implementation

SAMPLE INPUT:>>>
1
#B#A#
##BA#
OUTPUT:>>> Yes

SAMPLE INPUT:>>>
1
###B#A##
##A#B###
OUTPUT:>>> No
'''
#User function Template for python3
class Solution:
    def moveRobots (self, s1, s2):
        # code here 
        #if len os bots is not same they can never be transformed so return No
        if len(s1) != len(s2) : 
            return "No"
        bots = []
        #here below we are tracking the indices for the A &  B
        for i in range(len(s1)):
            if s1[i] != '#':
                bots.append(i)
        b = 0
        #b will increase only when the j loop approaches A or B
        #the below condition is said to return No if b is len(bots) it means
        #we did already approached A and B in s2 and need to terminate the loop
        #and as they cannot cross each other we need to check the approaches
        #of two bots are same for A and B and third condition is used to check whether A is
        #moving to the right side and 4th for B is moving to the left side in those cases 
        # we return cases we return No and at end if b == len(bots) we can return "yes"
        for j in range(len(s2)):
            if s2[j] != '#':
                if b == len(bots) or s2[j] != s1[bots[b]] or\
                (s2[j] == 'A' and j > bots[b]) or\
                (s2[j] == 'B' and j < bots[b]):
                    #print(b,j)
                    return 'No'
                b+=1
        return "Yes" if b == len(bots) else "No"
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s1 = input()
        s2 = input()

        ob = Solution()
        print(ob.moveRobots(s1, s2))

# } Driver Code Ends