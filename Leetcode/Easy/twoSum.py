#problem : https://leetcode.com/problems/two-sum
#This is a O(N) solution with space complexity trade-off
# with O(1) space sorting followed by two-pointers or binary search each of n elements would work with O(NlogN) time complexity

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return 
        num_dict ={}
        current = 0
        while current<len(nums):
            if target - nums[current] in num_dict:
                return [num_dict[target-nums[current]],current]
            else:
                num_dict[nums[current]] = current
                current+=1
        return