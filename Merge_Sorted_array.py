#WIP
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr=[None]*(m+n)
        i=0
        while (i<m):
            arr[i]=nums1[i]
            i+=1
        
        k=0
        h=0
        j=0
        for k in range (m+n):
            print(k)
            print(j)
            print(h)
            if(arr[j]<=nums2[h]):
                nums1[k]=arr[j]
                j+=1
                print("asd",nums1)
            
            elif(arr[j]>nums2[h]):
                nums1[k]=nums2[h]
                h+=1
                print(nums1)
