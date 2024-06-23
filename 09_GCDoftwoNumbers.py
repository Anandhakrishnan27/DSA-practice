
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        while b:
            a, b = b, a % b
        return a
        