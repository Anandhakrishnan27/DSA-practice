class Solution:
    def countTriples(self, n: int) -> int:
        res=0
        limit=n*n
        for i in range(1,n):
            for j in range(i+1,n):
                k=i*i + j*j
                if k > limit: break
                print(k)
                if sqrt(k)%1==0:
                    res+=2
        return res