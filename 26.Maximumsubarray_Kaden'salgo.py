class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            max_nums=nums[0]
            max_so_far=nums[0]
            for num in nums[1:]:
              max_nums=max(num,max_nums+num)
              max_so_far=max(max_nums,max_so_far)   
            return max_so_far  
      