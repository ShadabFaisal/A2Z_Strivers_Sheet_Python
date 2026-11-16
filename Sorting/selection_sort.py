class Solution:
    def selection_sort(self, nums: list[int])-> list[int]:
        n=len(nums)
        for i in range(0,n-1):
            mini=i
            for j in range(i,n):
                if nums[j]<nums[mini]:
                    mini=j

            nums[i],nums[mini]=nums[mini],nums[i]

        return nums




# Driver code
if __name__ == "__main__":
    # Input array
    nums = [29, 10, 14, 37, 13]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    answer = obj.selection_sort(nums)
    print(answer)