'''
Level:>>> Medium
Geek is at the geek summer carnival. To unlock discounts on exclusive courses he is given a card with a binary tree, a target node and a positive integer k on it. 
He needs to find the sum of all nodes within a max distance k from target node such that the target node is included in sum.

Example 1:

Input:
target = 9 
k = 1
Binary Tree = 
            1
           /  \
          2    9
        /     /  \
       4     5    7
      /  \       /  \
     8    19    20   11
    /   /   \
  30   40   50

Output: 22

Explanation: 
Nodes within distance 1 from 9 
9 + 5 + 7 + 1 = 22

Example 2:

Input:
target = 40 
k = 2
Binary Tree = 
            1
           /  \
          2    9
        /     /  \
       4     5    7
      /  \       /  \
     8    19    20   11
    /   /   \
  30   40   50

Output: 113

Explanation:
Nodes within distance 2 from 40,
40 + 19 + 50 + 4 = 113
Your Task:
You don't need to read input or print anything. Complete the function sum_at_distK() that takes the root of the given binary tree, target and k as input parameters and return the required sum. 

Expected time complexity: O(n)
Expected space complexity: O(n)

Constraints:
1 <= number of nodes <= 1000
1 <= data in nodes,target <= 10000

Related Topics:>>>
Tree

SAMPLE INPUT:>>>
1
1 2 9 4 N 5 7 8 19 N N 20 11 30 N 40 50
9 1

OUTPUT:>>>
22
'''
class Solution:
    def sum_at_distK(self,root, target, k):
        def get_routes(node, parent_node, routes):
            if not node:
                return None
            
            routes[node] = parent_node
            if node.data == target:
                return node

            return get_routes(node.left, node, routes) or get_routes(node.right, node, routes)
        
        def travel(n, k, visited):
            if not n or n in visited or k < 0:
                return
            
            nonlocal s
            visited.add(n)
            s += n.data
            
            travel(n.left, k-1, visited)
            travel(n.right, k-1, visited)
        
        routes = {}
        initial = get_routes(root, None, routes)
        visited = set()
        s = 0
        while initial and k >= 0:
            travel(initial, k, visited)
            initial = routes[initial]
            k -= 1
        return s