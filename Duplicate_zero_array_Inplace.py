#WIP
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zc=0
        j=0
        for i in range(len(arr)):

            if(arr[i]==0 and (i+zc<len(arr))):
                zc+=1
            
        #new code
        if(arr[len(arr)-zc-1]==0):
            zc-=1
        #end of new code
        
        
        for i in range(len(arr)):
            
            if(arr[len(arr)-1-zc-i]!=0):
                arr[len(arr)-1-j]=arr[len(arr)-1-zc-i]
            
            #new code1
            #elif(arr[len(arr)-1-zc]==0):
            #   arr[len(arr)-1-j]=arr[len(arr)-1-zc-i]
            #end of new code1
            
            elif(arr[len(arr)-1-zc-i]==0):             
                arr[len(arr)-1-j]=arr[len(arr)-1-zc-i]
                j+=1
                arr[len(arr)-1-j]=arr[len(arr)-1-zc-i] 
             
            i+=1
            j+=1
