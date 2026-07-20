from collections import *
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited=set()
        def dfs(node):
            if node == destination :
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited and dfs(nei):
                    return True
            return False
        return dfs(source)
            
        