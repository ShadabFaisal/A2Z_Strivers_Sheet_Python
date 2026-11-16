class Solution:
    def bubble_sort(self, nums:list[int]):
        n=len(nums)
        for i in range(n-1):
            swapped=False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapped=True

            if not swapped:
                break


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [29, 10, 14, 37, 13]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    obj.bubble_sort(arr)
    print(arr)