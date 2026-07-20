
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[0]*len(isConnected)
        def dfs(node):
            visited[node]=1
            for nei in range(len(isConnected)):
                if isConnected[node][nei] == 1 and not visited[nei]:
                    dfs(nei)
        c=0
        for i in range(len(isConnected)):
            if  not visited[i]:
                dfs(i)
                c+=1
        return c
        