class Twitter:

    def __init__(self):
        # {a: [t1, t2, t3 ], b: [t3, t4]}
        self.userTweets = defaultdict(list)
        # to stamp tweets with time stamps
        # {t1:001, t2:002} to fast look up the timestamp of a tweet
        self.tweets = dict()
        # {A:[B, C]} userA follows user B & C
        self.userFollows = defaultdict(set)
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        time = self.timeStamp
        self.timeStamp += 1
        self.tweets[tweetId] = time
        self.userTweets[userId].append(tweetId)


        
    def getNewsFeed(self, userId: int) -> List[int]:
        # use a temp heap of capacity 10 to add all tweets possible to be displayed
        feedHeap = [(self.tweets[tw], tw) for tw in self.userTweets[userId][-10:]]
        heapq.heapify(feedHeap)
        for followee in self.userFollows[userId]:
            for tw in self.userTweets[followee][-10:]:
                heapq.heappush(feedHeap, (self.tweets[tw], tw))
                if len(feedHeap) > 10:
                    heapq.heappop(feedHeap)
        feedsToShow = []
        while feedHeap:
            time, tw = heapq.heappop(feedHeap)
            feedsToShow.append(tw)
        feedsToShow.reverse()
        return feedsToShow


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.userFollows[followerId]:
            return
        self.userFollows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)