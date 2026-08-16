class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        path, seen = set(), set()

        def dfs(node: int) -> bool:
            if node in path:
                return False
            
            if node in seen:
                return True
            
            path.add(node)

            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
                
            path.remove(node)
            seen.add(node)

            return True
            
        for course in range(numCourses):

            # If there is a cycle or course you
            # cannot take
            if not dfs(course): return False
        
        return True
        
