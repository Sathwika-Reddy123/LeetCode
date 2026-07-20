class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        indegree=[0]*len(quiet)
        graph=defaultdict(list)
        for x,y in richer:
            graph[x].append(y)
            indegree[y]+=1
        q=deque()
        res=[i for i in range(len(quiet))]
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        while q:
            x=q.popleft()
            for y in graph[x]:
                if quiet[res[x]]<quiet[res[y]]:
                    res[y]=res[x]
                indegree[y]-=1
                if indegree[y]==0:
                    q.append(y)
        return res
     
        