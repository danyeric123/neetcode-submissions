class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj_list = defaultdict(list)

        for req, pre in prerequisites:
            adj_list[req].append(pre)
        
        # We have seen and path because we 
        # want to keep track of what prereq
        # was already done (=seen) but we don't
        # want it to be circular (=path)
        seen, path = set(), set()

        def dfs(node: int) -> bool:
            # We want to make sure we propogate
            # the boolean up the stack

            # Base case
            if node in path:
                return False
            if node in seen:
                return True
            
            path.add(node)
            # recursive
            for pre in adj_list[node]:
                if not dfs(pre): return False
            
            path.remove(node)
            seen.add(node)
            res.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i): return []
        
        return res