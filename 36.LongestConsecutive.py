class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0

        nums.sort()
        longest,current_longest=1,min(1,len(nums))
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                current_longest+=1
            else:
                current_longest=1
            longest=max(longest,current_longest)
        return longest


        