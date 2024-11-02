class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1] : return False
        sList = sentence.split(" ")

        for i in range(0, len(sList)-1):
            if sList[i][-1] != sList[i+1][0]:
                return False

        return True
        