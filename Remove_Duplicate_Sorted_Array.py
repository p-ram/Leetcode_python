#passes all test cases

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        #array of unique number index
        arr=[0]

        #main loop
        i=0
        
        #null input
        if(len(nums)==0):
            k=0
            return k
        else:
            pass
        
        while(i<len(nums)-1):
            
            # duplicate counter for each loop
            j=0
            
            # duplicate counter loop
            for m in range(i,len(nums)-1):
                
                if(nums[m]==nums[m+1]):
                    j+=1
                    
                    
                else:
                    
                    break
                
            #move pointer to next unique
            i=i+j+1
            
            
            #if i!= last element then append
            if(i!=len(nums)):
                arr.append(i)

        
        #main rearrange loop
        b=0
        for a in arr:
            
            nums[b]=nums[arr[b]]
            b+=1
                    
        # return k unique numbers
        k=len(arr)
        return k
            
        
