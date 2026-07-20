from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*(numCourses)
        graph=defaultdict(list)
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]+=1
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        c=0
        while q:
            x=q.popleft()
            c+=1
            for nei in graph[x]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if c==numCourses:
            return True
        else:
            return False


        