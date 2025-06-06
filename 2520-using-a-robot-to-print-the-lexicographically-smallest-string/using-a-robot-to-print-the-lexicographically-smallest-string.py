class Solution:
    def robotWithString(self, s: str) -> str:
        n=len(s)
        st=[]
        result=[]
        min_ = ['{'] * n
        for i in range(n - 2, -1, -1):
            min_[i] = min(s[i + 1], min_[i + 1])
        for i, ch in enumerate(s):
            st.append(ch)
            while st and st[-1] <= min_[i]:
                result.append(st.pop())
        while st:
            result.append(st.pop())
        return ''.join(result)
