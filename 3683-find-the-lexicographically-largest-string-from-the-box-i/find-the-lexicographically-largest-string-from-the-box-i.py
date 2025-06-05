class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        max=""
        for i in range(len(word)):
            s=word[i:i+len(word)-numFriends+1]
            if s>max:
                max=s
        return max
        