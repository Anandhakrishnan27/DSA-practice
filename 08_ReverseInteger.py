##Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
      reverse=0
      sign = -1 if x < 0 else 1
      x=abs(x)
      while x!=0:
        digit=x%10
        reverse=reverse*10+digit
        x//=10
      if reverse > 2**31 - 1 or reverse < -2**31:
            return 0
        
      return reverse*sign