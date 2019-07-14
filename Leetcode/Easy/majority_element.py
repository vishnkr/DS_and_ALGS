# Problem Statement: https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majorityIndex = len(nums)//2
        return nums[majorityIndex]
        