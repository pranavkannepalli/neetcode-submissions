class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        queue = collections.deque()
        neighbors = {i: [] for i in range(numCourses)}
        
        for i in prerequisites:
            indegrees[i[0]] += 1
            neighbors[i[1]].append(i[0])
        
        for index, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(index)
        
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for i in neighbors[curr]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
                elif indegrees[i] < 0:
                    return []

        return res if len(res) == numCourses else []