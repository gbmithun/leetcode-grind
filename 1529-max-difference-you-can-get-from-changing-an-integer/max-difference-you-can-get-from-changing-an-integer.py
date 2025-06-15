class Solution:
    def maxDiff(self, num: int) -> int:
        n = str(num)
        i = 0
        while i < len(n) and n[i] == "9":
            i += 1
        if i < len(n):
            maxi = n.replace(n[i], "9")
        else:
            maxi = n
        if n[0] != '1':
            mini = n.replace(n[0], '1')
        else:
            found = False
            for j in range(1, len(n)):
                if n[j] != '0' and n[j] != '1':
                    mini = n.replace(n[j], '0')
                    found = True
                    break
            if not found:
                mini = n
        return int(maxi) - int(mini)
