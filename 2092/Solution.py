class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # graph[i] = all (time, person) tuples
        # for ith person's meetings
        graph = defaultdict(list)
        
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))
        
        # earliest[i] = earliest time ith person has the secret
        earliest = [inf] * n
        
        earliest[0] = 0
        earliest[firstPerson] = 0

        # store (person, meeting time)
        q = deque()
        
        q.append((0, 0))
        q.append((firstPerson, 0))

        while q:
            person, time = q.popleft()
            
            for nextTime, nextPerson in graph[person]:
                # add a new node to visit only if 
                # earliest secret time must be updated
                if nextTime >= time and earliest[nextPerson] > nextTime:
                    earliest[nextPerson] = nextTime
                    q.append((nextPerson, nextTime))
        
        visited = []
        
        for i in range(n):
            if earliest[i] != inf:
                visited.append(i)
        
        return visited
