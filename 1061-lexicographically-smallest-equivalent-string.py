class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p = list(range(26))

        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]

        for i in range(len(s1)):
            ss1,ss2=ord(s1[i])-ord("a"),ord(s2[i])-ord("a")
            pss1,pss2=find(ss1),find(ss2)
            if pss1>pss2:
                p[pss1]=pss2
            else:
                p[pss2]=pss1

        r=[]
        for c in baseStr:
            ci=ord(c)-ord("a")
            r.append(chr(find(ci)+ord('a')))
        return "".join(r)
