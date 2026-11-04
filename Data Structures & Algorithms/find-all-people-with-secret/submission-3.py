class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = {0, firstPerson}
        time_map = defaultdict(lambda: defaultdict(list))

        for p1, p2, t in meetings:
            time_map[t][p1].append(p2)
            time_map[t][p2].append(p1)

        for t in sorted(time_map):
            adj = time_map[t]
            visited = set()
            stack = [p for p in adj if p in secrets]

            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                secrets.add(node)
                for nei in adj[node]:
                    if nei not in visited:
                        stack.append(nei)

        return list(secrets)