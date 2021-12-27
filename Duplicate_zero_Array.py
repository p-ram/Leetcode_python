class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        new=[]
        i=0
        count=0
        while(count<len(arr)):
            
            if(arr[i]==0):
                new.append(0)
                count+=1
                if count>=len(arr):
                    break
                new.append(0)
                #print(new)
                count+=1
            
            elif(arr[i]!=0):
                new.append(arr[i])
                count+=1
                   
            i+=1
        
        for i in range(len(new)):
            arr[i]=new[i]
        #return new
