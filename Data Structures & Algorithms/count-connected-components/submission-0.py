class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comps = 0
        adj = [[] for _ in range(n)]
        notVisited = set()

        for i in range(n):
            notVisited.add(i)
        
        # from adjacency list
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def dfs(curr):
            notVisited.discard(curr)
            for i in adj[curr]:
                if i in notVisited:
                    dfs(i)
        
        curr = None
        while len(notVisited) > 0:
            curr = next(iter(notVisited))
            comps += 1
            dfs(curr)

        return comps