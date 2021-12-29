#

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #j pointed to last 
        j=len(nums)-1
        
        #k is total elements shifted to last
        k=0
        i=0
        
        while((i-j<=0)):
            
            #last num is val
            if(i==j and nums[i]==val):
                k+=1
                i+=1
                print("--1--")
                print(i)
                print(j)
                print("----------")
                
                       
            elif(nums[i]==val):
                temp = nums[i]
                #nums[i]=nums[i+1]
                
                
                #shift remaining elements to left
                for m in range (i, len(nums)-1):
                    nums[m]=nums[m+1]
                
                
                k+=1
                nums[j]=temp
                j-=1
                
                print("before",i)
                #check if nums[i+1]=val and dont increment i
                if(nums[i+1]==val):
                    break
                
                print("after",i)
                
                print(j)
                print("----------")
                
            
            elif(nums[i]!=val):
                i+=1
                print("--2--")
                print(i)
                print(j)
                print("----------")
        
        print("end of while")
        print(k)
        print(nums)
        
        return
