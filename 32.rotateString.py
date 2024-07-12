class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = s
        for i in range(len(s)):
            temp = temp[1:] + temp[0]

            if temp == goal:
                return True
        return False
