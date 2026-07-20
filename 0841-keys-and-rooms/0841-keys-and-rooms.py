class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        q=deque()
        q.append(0)
        while q:
            x=q.popleft()
            visited.add(x)
            for nei in rooms[x]:
                if nei not in visited:
                    q.append(nei)
        if len(rooms)==len(visited):
            return True
        else:
            return False
        