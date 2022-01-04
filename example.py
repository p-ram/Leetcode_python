#testing branch in GIT

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
        
        while(i<len(nums)-1):
            
            # duplicate counter for each loop
            j=0
            print("i",i)
            # duplicate counter loop
            for m in range(i,len(nums)-i+1):
                print("m",m)
                if(nums[m]==nums[m+1]):
                    j+=1
                    print("j",j)
                else:
                    break
            
            
            
            
            #move pointer to next unique
            i=i+j+1
            print("-----i-----",i)
            arr.append(i)
        
        
        
        
        print("----------------",arr)
        #main rearrange loop
        
        b=0
        for a in arr:
            #print("a",a)
            #print("nums before",nums)
            nums[b]=nums[arr[b]]
            b+=1
            #print("b",b)
            #print("nums after",nums)
        
        # return k unique numbers
        k=len(arr)
        return k
            
        
