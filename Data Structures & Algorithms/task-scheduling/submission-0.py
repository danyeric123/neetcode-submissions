class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(N * n) where n is the idle time
        # since we have to go through all the tasks
        # and have a wait time of n

        time = 0

        task_counts = Counter(tasks)
        
        # Strategy: Always execute most frequent task to minimize
        # future idle time
        # Use heap for ready tasks, queue for tasks on cooldown
        # O(log 26). We will be switching between the two
        min_heap = [-c for c in task_counts.values()]

        heapq.heapify(min_heap)

        # We have: 
        # one heap for keeping track of which task has more
        # a queue for keeping track of when the task is up
        cooldown = deque()

        while min_heap or cooldown:
            # We have a while loop to mimic
            # CPU cycles so we increment time
            # to keep track at the beginning
            # which cycle we are on
            time += 1

            # check if we can pull off queue to "schedule"
            # and if min_heap is empty than don't need to pull
            # from here (but may have need to pull from cooldown)
            if min_heap:
                # decrement count, which is opposite since negative
                count = 1 + heapq.heappop(min_heap)
                if count:
                    cooldown.append((count, time + n))
                
            # check if time for front of queue
            if cooldown and cooldown[0][1] == time:
                # Grab the count since the wait is over
                heapq.heappush(min_heap, cooldown.popleft()[0])
            
            # if neither conditional is true, then this 
            # is just an idle period


            
        return time
