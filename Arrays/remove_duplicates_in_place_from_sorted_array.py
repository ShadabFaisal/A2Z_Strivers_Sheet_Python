class Solution:
    def remove_duplicates_from_sorted_array(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0

        j=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1

        return j

        


if __name__ == "__main__":
    nums = [1,1,2,3,4,4]
 
    solution = Solution()
    print("Length of array after removing duplicates:", solution.remove_duplicates_from_sorted_array(nums))