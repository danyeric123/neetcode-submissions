class Twitter:

    def __init__(self):
        self.time = 0 # count is basically keeping track of time
        self.tweet_map = defaultdict(list) # userId -> list of [count, tweetIds]
        self.follow_map = defaultdict(set)  # userId -> set of followeeId
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        # First get the most recent tweets from all the followees,
        # including self
        # Get only the most recent
        self.follow_map[userId].add(userId)
        # O(k) to go through the list
        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                time, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap, (time, tweet_id, followee_id, index - 1))
        
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

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followeeId not in self.follow_map[followerId]
        ):  # Can't unfollow someone who you are not already following
            return None
        self.follow_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)