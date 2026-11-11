class Solution:
    def second_largest_element(self, nums: list[int]) -> int:
        max_num=nums[0]
        second_largest=-1
        for num in nums:
            if num >max_num:
                second_largest=max_num
                max_num=num
            elif num>second_largest and num!=max_num:
                second_largest=num
        return second_largest


if __name__ == "__main__":
    nums = [14 ,135, 2, 9, 1]
 
    solution = Solution()

    print("Second Largest element:", solution.second_largest_element(nums))   