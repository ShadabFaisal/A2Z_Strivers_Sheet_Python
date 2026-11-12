class Solution:
    def left_rotate_by_one_place(self, nums):
        temp = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[-1] = temp
        return nums





if __name__ == "__main__":
    nums = [1,2,3,4,5]
 
    solution = Solution()
    result = solution.left_rotate_by_one_place(nums)
    print(result)