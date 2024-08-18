class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x = -1
        d = dict()
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        for key,value in d.items():
            if key == value:
                x = key
        return x
        