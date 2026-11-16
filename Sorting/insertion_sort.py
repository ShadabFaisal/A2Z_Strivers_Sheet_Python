class Solution:
    def insertion_sort(self,nums:list[int]):
        n=len(nums)
        for i in range(n):
            j=i
            while j>0 and nums[j-1]>nums[j]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [29, 10, 14, 37, 13]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    obj.insertion_sort(arr)
    print(arr)