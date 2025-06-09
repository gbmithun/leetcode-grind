class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        from collections import deque
        n = len(status)
        visited = [False] * n
        have = set(initialBoxes)
        queue = deque()
        res = 0

        while True:
            progress = False
            for box in list(have):
                if status[box] and not visited[box]:
                    visited[box] = True
                    res += candies[box]
                    for k in keys[box]:
                        status[k] = 1
                    for b in containedBoxes[box]:
                        have.add(b)
                    progress = True
            if not progress:
                break
        return res
