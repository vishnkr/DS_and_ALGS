#problem statement : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        counter = 0
        for val in range(1,len(nums)):
            if nums[val] != nums[counter]:
                counter+=1
                nums[counter]=nums[val]
        return counter+1