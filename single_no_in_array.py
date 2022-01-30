class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        adict={nums[0]:1}
                
        for c, val in enumerate(nums[1:]):
            
            if val in adict:
                adict[val]+=1
            else:
                adict[val]=1
        
               
        return adict.keys()[list(adict.values()).index(1)]
            
