class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adj_list = defaultdict(list)

        for par, child in edges:
            adj_list[par].append(child)
            adj_list[child].append(par)
        
        def dfs(curr: int, par: int) -> int:
            time = 0
            for child in adj_list[curr]:
                # skip parents since we 
                # don't just want to go back to
                # parents
                if child == par: continue

                child_time = dfs(child, curr)
                # if we have a value or this has
                # an apple then we need to visit
                # and come back
                if child_time > 0 or hasApple[child]:
                    # we accumulate the time for
                    # collecting apples in this subtree
                    time += 2 + child_time
            
            return time
        
        return dfs(0, -1)