# code working for normal cases, edge cases WIP
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # k count for new nums1 
        # i count for nums1
        # j count for nums2
        k=0
        i=0
        j=0
        
        #duplicate array nums1
        arr=[None]*(m+n)
        for w in range (len(nums1)):
            arr[w]=nums1[w]
        #end duplicate array
        
        
        for k in range (m+n):
            
            if(nums1[i]<=nums2[j] and i<(m)):
                nums1[k]=arr[i]
                i+=1
                print("1",nums1)
                 
                
            elif(nums1[i]>nums2[j] and j<(n)):
                nums1[k]=nums2[j]
                j+=1
                print("2",nums1)
                
            
            elif(i==(m) and j<(n)):
                nums1[k]=nums2[j]
                j+=1
                print(k)
                print(j)
                print("3",nums1)
                
            
            elif(j==(n)):
                nums1[k]=arr[i]
                i+=1
                print("4",nums1)
                
            print("k",k)
            print("i",i)
            print("j",j)
            print("----------------------")
            
