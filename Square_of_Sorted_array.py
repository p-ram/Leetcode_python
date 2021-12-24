class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
                 
        i=0
        j=len(nums)-1
        new_list=[None]*len(nums)
        
        
        for n in range(len(nums)):
            if(pow(nums[i],2)<=pow(nums[j],2)):
                new_list[len(nums)-n-1]=pow(nums[j],2)
                
                """"print("j",j)
                print("i",i)"""
                j-=1

            elif(pow(nums[i],2)>pow(nums[j],2)):
                new_list[len(nums)-n-1]=pow(nums[i],2)

                """"print("i",i)
                print("j",j)"""
                i+=1

            
        return new_list   