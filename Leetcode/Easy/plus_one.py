#Problem Link - https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total=0
        arr=[]
        string=''
        for i in digits:
            string+=str(i)
        total=int(string)+1
        return [int(x) for x in str(total)]
     
        