class Solution:

    def find_number_appearing_once(self, nums: list[int])->int:
        xor1=0
        for i in range(len(nums)):
            xor1^=nums[i]

        return xor1



if __name__ == "__main__":
    nums = [1,2,2,3,3,4,4]
  
    solution = Solution()
    result = solution.find_number_appearing_once(nums)
    print(f"Number Appearing Once: {result}")