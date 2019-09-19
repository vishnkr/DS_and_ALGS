class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        aCount = 0
        bCount = 0
        sum=0
        n = len(costs)//2
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        for i in costs:
            if (i.index(min(i[0],i[1]))==0 and aCount!=n) or bCount==n:
                aCount+=1
                sum+=i[0]
            else:
                bCount+=1
                sum+=i[1]
        return sum