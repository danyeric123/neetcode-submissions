class Twitter:

    def __init__(self):
        self.time = 0 # count is basically keeping track of time
        self.tweet_map = defaultdict(list) # userId -> list of [count, tweet_ids]
        self.follow_map = defaultdict(set)  # userId -> set of followee_id
        

    def postTweet(self, userId: int, tweet_id: int) -> None:
        self.tweet_map[userId].append((self.time, tweet_id))
        if len(self.tweet_map[userId]) > 10:
            # we only need to keep the latest 10 since getNewsFeed 
            # only cares about 10
            self.tweet_map[userId].pop(0)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        # First get the most recent tweets from all the followees,
        # including self
        # Get only the most recent
        self.follow_map[userId].add(userId)
        # O(k) to go through the list, but since
        # we will only have 10 at most in heap, it 
        # becomes O(k * log(10)), which is the same 
        # as O(k)
        max_heap = []
        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                time, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(max_heap, (-time, tweet_id, followee_id, index - 1))
                if len(max_heap) > 10:
                    heapq.heappop(max_heap)
        while max_heap:
            time, tweet_id, followee_id, index = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-time, tweet_id, followee_id, index))
        
        # Pull the tweets from each user in chronological order
        # starting with the most recent we pulled and moving down
        # the tweet list for each and adding the next recent to the heap
        while min_heap and len(res) < 10:
            time, tweet_id, followee_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            if index >= 0:
                time, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap, (time, tweet_id, followee_id, index - 1))
            
        return res

    def follow(self, followerId: int, followee_id: int) -> None:
        self.follow_map[followerId].add(followee_id)
        

    def unfollow(self, followerId: int, followee_id: int) -> None:
        if (
            followee_id not in self.follow_map[followerId]
        ):  # Can't unfollow someone who you are not already following
            return None
        self.follow_map[followerId].remove(followee_id)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweet_id)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followee_id)
# obj.unfollow(followerId,followee_id)