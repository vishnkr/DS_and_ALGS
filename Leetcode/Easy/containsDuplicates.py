#problem: https://leetcode.com/problems/contains-duplicate


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        if len(nums)==0:
            return False
        
        for i in nums:
            if i in dict and dict[i]==1:
                return True
            else:
                dict[i]=1
        return False