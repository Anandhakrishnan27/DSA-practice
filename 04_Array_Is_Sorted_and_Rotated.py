##Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
class Solution:
    def check(self, nums: List[int]) -> bool:
       print(sorted(nums))
       if(nums==sorted(nums)):
         return True
       a=1
       b=len(nums)
       while(a<b):
          c=nums[b-a:]+nums[:b-a]
          if(c==sorted(nums)):
            return True
          else:
            a+=1
       return False
       
