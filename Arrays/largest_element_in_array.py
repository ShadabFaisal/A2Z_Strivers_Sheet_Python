class Solution:
    def largest_element(self, nums: list[int]) -> int:
        max_num=nums[0]
        for num in nums:
            if num >max_num:
                max_num=num
        return max_num


if __name__ == "__main__":
    nums = [14 ,135, 2, 9, 1]
 
    solution = Solution()

    print("Largest element:", solution.largest_element(nums))   