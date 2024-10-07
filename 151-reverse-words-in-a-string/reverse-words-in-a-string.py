class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split(" ")
        ans = []
        while list_s:
            last = list_s.pop()
            if last.isalnum():
                ans.append(last)

        return " ".join(ans)



        