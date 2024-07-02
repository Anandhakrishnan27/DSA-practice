class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        m = defaultdict(int)
        for num in nums:
            m[num]+=1
        n=n//2
        print(m.items())
        for key,value in m.items():
            if value>n:
                return key
        return 0