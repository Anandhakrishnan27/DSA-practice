class Solution:
    def sortByBit(self, arr: List[int]) -> List[int]:
            return sorted(arr, key=lambda v: (bin(v).count('1'), v))   

        
