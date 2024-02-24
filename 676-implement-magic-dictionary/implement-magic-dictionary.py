class MagicDictionary:

    def __init__(self):
        self.dick = dict()
        
    def buildDict(self, dictionary: List[str]) -> None:
        
        for s in dictionary:
            if len(s) not in self.dick.keys():
                self.dick[len(s)] = [s]
            else:
                self.dick[len(s)].append(s)


    def search(self, searchWord: str) -> bool:
        #Edge case
        if len(searchWord) not in self.dick:
            return False

        # for k, v in self.dick.items():
        #     print(k, v)

        b = self.dick[len(searchWord)]


        for word in b:
            counter = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    counter += 1
            if counter == 1:
                return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

