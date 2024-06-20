##Contains Duplicate
##Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
  def containsDuplicate(self, nums) -> bool:
        s = set(nums)
        if(len(nums) == len(s)):
            return False
        else:
            return True
if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.containsDuplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.containsDuplicate(nums2)) # Expected output: True
