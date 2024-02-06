class Codec:
    def __init__(self):
        self.shortToLong = dict()
        self.longToShort = dict()
        self.chars = "abcdefghijklmnopqrstuvwxyz0123456789"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.longToShort:
            while True:
                code = "".join([random.choice(self.chars) for _ in range(6)])
                if code not in self.shortToLong:
                    self.shortToLong[code] = longUrl
                    self.longToShort[longUrl] = code
                    break
        
        return self.longToShort[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.shortToLong[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))