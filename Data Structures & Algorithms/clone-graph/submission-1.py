"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a map of duplicate nodes, from og node to duplicate node 
        # dfs - post order assignment
        # traverse original graph, at a given node, assign the neighbors of the node 
        # bfs process the node when queueing ujp the neighbors assign the neighbors
        if not node:
            return None
        clones = {}  
        self.dfs(node, clones)
        return clones[node]

    def dfs(self, node, clones):
        if node is None:
            return None
        if node in clones:
            return

        clones[node] = Node(node.val, None)

        for nei in node.neighbors:
            self.dfs(nei, clones)
            # What about cycles
            clones[node].neighbors.append(clones[nei])
        
