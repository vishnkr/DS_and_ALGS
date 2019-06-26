class Solution:
    def rob(self, nums: List[int]) -> int:
        
        last = 0
        current = 0
        
        for i in nums:
            last,current = current, max(last + i, current)
                
        return current