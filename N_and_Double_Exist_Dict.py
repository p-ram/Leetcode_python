#passes all test case

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #create dict
        dict={}
        
        #edge case zero counter
        zero=0
        
        
        #main
        
        for i,n in enumerate(arr):
            
            #key=arr, value=index
            dict[n]=i
            #print("init",n)
            
            if(i==0):
                #print('start')
                if(n==0):
                    zero+=1
                    #print("i = zero")
                continue
            
            elif(n==0):
                #print("zero")
                zero+=1
                if(zero>1):
                    return True
   
            
            elif(n*2 in dict and n!=0):
                #print("1")
                return True
            
            elif(n/2 in dict and n%2==0 and n!=0):
                #print("2")
                return True
                
            else:
                #print("---------")
                #print("mod",n%2)
                #print("div",n/2)
                #print("not found")
                continue
        
        return False
            
