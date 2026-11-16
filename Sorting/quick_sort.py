class Solution:
    def quick_sort(self, nums:list[int], low:int, high:int):
        # low =0, high=7  
        if low>=high:
            return
        pivotIndex=self._partitionArray(nums,low, high)
        self.quick_sort(nums, low, pivotIndex-1)
        self.quick_sort(nums, pivotIndex+1,high)



    def _partitionArray(self, nums:list[int], low:int, high:int)-> int:
        pivot=nums[low]
        i=low
        j=high

        while i<j:
            while nums[i]<=pivot and i<=high:
                i+=1
            while nums[j]>pivot and j>=low:
                j-=1

            if i<j:
                nums[i],nums[j]=nums[j],nums[i]

        nums[low],nums[j]=nums[j],nums[low]
        return j


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [4,6,2,5,7,9,1,3]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    obj.quick_sort(arr, 0, len(arr)-1)
    print(arr)