'''
!!!!!!!SOLUTION IS IN C++!!!!!!!!!!!
Level:>>> Medium
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches is as small as possible.
Let us first define the cost of a BST. The cost of a BST node is level of that node multiplied by its frequency. Level of root is 1.


Example 1:

Input:
n = 2
keys = {10, 12}
freq = {34, 50}
Output: 118
Explaination:
There can be following two possible BSTs 
        10                       12
          \                     / 
           12                 10
                              
The cost of tree I is 34*1 + 50*2 = 134
The cost of tree II is 50*1 + 34*2 = 118 

Example 2:


Input:
N = 3
keys = {10, 12, 20}
freq = {34, 8, 50}
Output: 142
Explaination: There can be many possible BSTs
     20
    /
   10  
    \
     12  
     
Among all possible BSTs, 
cost of this BST is minimum.  
Cost of this BST is 1*50 + 2*34 + 3*8 = 142

Your Task:
You don't need to read input or print anything. Your task is to complete the function optimalSearchTree() which takes the array keys[], freq[] and their size n as input parameters and returns the total cost of all the searches is as small as possible.


Expected Time Complexity: O(n3)
Expected Auxiliary Space: O(n2)


Constraints:
1 ≤ N ≤ 100

Related Topics:>>>
Binary Search Tree
Dynamic Programming

SAMPLE INPUT:>>>
1
2
10 12
34 50
OUTPUT:>>> 118
'''
// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution{
   public:
   int dp[101][101][101];
   int sol(int k[],int f[],int l,int r,int h)
   {
       if(l>r)
       return 0;
       
       if(dp[l][r][h]!=-1)
       return dp[l][r][h];
       
       int t=INT_MAX;
       for(int i=l;i<=r;i++)
       {
           t=min(t,h*f[i]+sol(k,f,l,i-1,h+1)+sol(k,f,i+1,r,h+1));
       }
       return dp[l][r][h]=t;
   }
   int optimalSearchTree(int keys[], int freq[], int n)
   {
       memset(dp,-1,sizeof dp);
       return sol(keys,freq,0,n-1,1);
   }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin >> n;
        int keys[n];
        for(int i=0;i<n;i++)cin>>keys[i];
        int freq[n];
        for(int i=0;i<n;i++)cin>>freq[i];
        Solution ob;
        cout<<ob.optimalSearchTree(keys, freq, n)<<endl;
    }
    return 0;
}  // } Driver Code Ends