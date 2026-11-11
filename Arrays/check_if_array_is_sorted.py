class Solution:
    def check_if_array_is_sorted(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True


if __name__ == "__main__":
    nums = [1,2,3,4,5]
 
    solution = Solution()
    
    print("Is the array sorted?:", solution.check_if_array_is_sorted(nums))