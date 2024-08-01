class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
         #Sorting nums in descending order
        nums.sort(reverse=True)

        return (nums[0]*nums[1]) - (nums[-1]*nums[-2]) 