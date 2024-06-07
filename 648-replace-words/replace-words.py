class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        def findRoot(roots: List[str], target:str) -> str:
            for root in sorted(roots, key = len):
                n = len(root)
                if target[:n] == root:
                    return root
            return target

        # dictionary as alphabetic key : value
        # c:cat, b:bat, r:rat
        dictMap = defaultdict(list)
        for word in dictionary:
            key = word[0]
            dictMap[key].append(word)
        
        words = sentence.split()

        for i, w in enumerate(words):
            # if first letter is in dictMap, we may have a root
            # otherwise do not touch this ith index
            if w[0] in dictMap:
                # change with the possible root
                words[i] = findRoot(dictMap[w[0]], w)
        
        return " ".join(words)




