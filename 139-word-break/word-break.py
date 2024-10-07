class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wSet = set(wordDict)

        @cache
        def dfs(s:str) -> bool:
            # Edge case
            if s == "": return True

            for w in wordDict:
                if s.startswith(w):
                    l = len(w)
                    remainder = s[l:]
                    if dfs(remainder): 
                        return True

            return False

        
        return dfs(s) 