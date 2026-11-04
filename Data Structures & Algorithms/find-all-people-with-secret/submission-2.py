import sys
sys.setrecursionlimit(10**6)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # person 0 and firstPerson know the secret
        secrets = set([0,firstPerson])
        
        time_map = {}

        for p1, p2, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)
            
            time_map[time][p1].append(p2)
            time_map[time][p2].append(p1)
        
        def dfs(node, visited, adj):
            if node in visited: return

            visited.add(node)

            # now the person knows
            secrets.add(node)

            for nei in adj[node]:
                dfs(nei, visited, adj)
        
        for t in sorted(time_map.keys()):
            # for all the visited at this time
            # not each
            visited = set()

            for src in time_map[t]:
                if src in secrets:
                    dfs(src, visited, time_map[t])
        
        return list(secrets)
