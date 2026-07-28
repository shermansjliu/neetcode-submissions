class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # check if there are cycels
        # some ordering list. Put the leaves at end of the array 

        g = {}
        for i in range(numCourses):
            g[i] = []
        for c, pre_req in prerequisites:
            g[pre_req].append(c) 

        s = []
        v = {}
        for i in range(numCourses):
            if self.has_cycle(i,g, v, s):
                return [] 
        return s[::-1]
    def has_cycle(self,node, g, v, s):
        if v.get(node,0) == 1:
            return True
        if v.get(node,0) == 2:
            return False
        v[node] = 1 

        for nei in g[node]:
            if self.has_cycle(nei, g, v, s):
                return True
        v[node] = 2
        s.append(node)
        return False

        

         
