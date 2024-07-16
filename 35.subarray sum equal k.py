class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        l=len(nums)
        for i in range(l):
            for j in range(i,l):
                sub_arr=nums[i:j+1]
                if sum(sub_arr)==k:
                    ans+=1
        return ans