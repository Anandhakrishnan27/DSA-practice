class Solution:
    def getLastDigit(self, a, b):
        if b == '0':
            return 1
        
        a = int(a) % 10  # We only need the last digit of a
        b = int(b)
        
        if a == 0:
            return 0
        
        # Use the property of cyclic nature of last digits
        b = b % 4 if b % 4 != 0 else 4
        
        return pow(a, b, 10)