##Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:   
        i=0
        while (i<k):
             a=nums.pop()
             nums.insert(0, a)
             i+=1
        return nums