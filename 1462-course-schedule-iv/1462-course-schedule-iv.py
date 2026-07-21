from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        ans=[]
        prereq=[set() for i in range(numCourses)]
        for i,j in prerequisites:
            graph[i].append(j)
            indegree[j]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            x=q.popleft()
            for nei in graph[x]:
                prereq[nei].add(x)
                prereq[nei].update(prereq[x])
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        for x,y in queries:
            ans.append(x in prereq[y])
        return ans

    