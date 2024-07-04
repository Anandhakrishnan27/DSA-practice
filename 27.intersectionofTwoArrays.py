class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      # Count occurrences of numbers in both lists
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        print(count1)
        for num in count1.keys() & count2.keys():
          
            result.extend([num] * min(count1[num], count2[num]))
        
        return result