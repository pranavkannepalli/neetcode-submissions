class Twitter:

    def __init__(self):
        self.user_follows = {}
        self.user_tweets = {}
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        if userId in self.user_tweets:
            all_tweets = list(self.user_tweets[userId])
        if userId in self.user_follows:
            for i in self.user_follows[userId]:
                all_tweets += self.user_tweets[i]

        minheap = []
        for i in all_tweets:
            heapq.heappush(minheap, i)
            if len(minheap) > 10:
                heapq.heappop(minheap)
        
        l = len(minheap)
        ret = [0] * l
        for i in range(l):
            ret[l - i - 1] = heapq.heappop(minheap)[1]
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)
