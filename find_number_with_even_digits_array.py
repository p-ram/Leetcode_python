class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            if int(math.log10(nums[i])%2)==1:
                count+=1
        return count    
