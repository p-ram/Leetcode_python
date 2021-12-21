class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        maxi=0
        for i in range(len(nums)):
            if( nums[i]==1):
                count+=1
            else:
                count=0
                if (len(nums)-i-1 < maxi):
                    break
            maxi=max(maxi,count)
        
        
        return maxi