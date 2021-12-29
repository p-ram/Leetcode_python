#passes all test cases, not optimized - raw code
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #j pointed to last 
        j=len(nums)-1
        
        #vc is total elements shifted to last
        vc=0
        i=0
        
        while((i-j<=0)):
            
            #last num is val
            if(i==j and nums[i]==val):
                vc+=1
                i+=1
                          
            elif(nums[i]==val):
                temp = nums[i]
                
                #shift remaining elements to left
                for m in range (i, len(nums)-1):
                    nums[m]=nums[m+1]
                
                vc+=1
                nums[j]=temp
                j-=1
                
                #check if nums[i+1]=val and dont increment i
                if(nums[i+1]==val):
                    continue
                           
            elif(nums[i]!=val):
                i+=1
        
        k=len(nums)-vc
        
        return k
