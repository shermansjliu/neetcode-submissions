from queue import Queue

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        # weighted graph
        # minimum time for all of the n nodes to receiv ethe signal 
        # k is the node that the node will be sent from 
        q = Queue()
        graph = {}

        min_dist_to_node = {}
        for i in range(1, n+1):
            graph[i] = []
            min_dist_to_node[i] = float('inf')

        for start, end, weight in times:
            graph[start].append((end, weight))

        q.put((k, 0))
        min_dist_to_node[k] = 0

        while not q.empty():
            node, distance = q.get()

            if distance > min_dist_to_node[node]:
                continue
            
            for nei, nei_weight in graph[node]:
                new_dist = distance + nei_weight
                if new_dist < min_dist_to_node[nei]:
                    min_dist_to_node[nei] = new_dist
                    q.put((nei, new_dist))
        
        max_time = max(min_dist_to_node.values())
        return max_time if max_time != float('inf') else -1
