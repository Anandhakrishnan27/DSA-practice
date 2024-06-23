#User function Template for python3
class Solution:
    def isPrime (self, N):
        # code here
        if(N<2):
            return 0
        for i in range(2,N):
            if(N%i==0):
                return 0
        return 1
