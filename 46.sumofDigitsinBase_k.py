class Solution:
    def sumBase(self, n: int, k: int) -> int:
        output_sum = 0
        while (n > 0) :
            rem = n % k
            output_sum = output_sum + rem 
            n = int(n / k)
        return output_sum
# Example 1:

# Input: n = 34, k = 6
# Output: 9
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.