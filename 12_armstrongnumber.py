
class Solution:
    def armstrongNumber (self, n):
        # code here 
        a=n
        val=0
        while (n!=0):
            num=n%10
            val+=pow(num,3)
            n//=10
        if(val==a):
            return 'true'
        else:
            return 'false'
       
