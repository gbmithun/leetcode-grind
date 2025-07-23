class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        return (self.fun(s,"ab",x,"ba",y) if x>=y else self.fun(s,"ba",y,"ab",x))
    def fun(self,s,str1,pt1,str2,pt2)->int:
        points=0
        st1=[]
        st2=[]
        for c in s:
            if st1 and st1[-1]==str1[0] and c==str1[1]:
                st1.pop()
                points+=pt1
            else:
                st1.append(c)
        for c in st1:
            if st2 and st2[-1]==str2[0] and c==str2[1]:
                st2.pop()
                points+=pt2
            else:
                st2.append(c)
        return points
        