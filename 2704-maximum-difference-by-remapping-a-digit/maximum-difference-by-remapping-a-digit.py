class Solution:
    def minMaxDifference(self, num: int) -> int:
        n=str(num)
        i=0
        while i<len(n) and n[i]=='9':
            i+=1
        if i<len(n):
            maxi=n.replace(n[i],'9')
        else:
            maxi=n
        mini=n.replace(n[0],'0')
        return int(maxi)-int(mini)