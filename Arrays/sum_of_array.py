class Solution:
    def find_sum_of_array(self, nums:list[int])->int:
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]

        return sum



if __name__=="__main__":
    nums=[1,22,31,4,5,16]

    solution=Solution()
    sum=solution.find_sum_of_array(nums)
    print(f"Sum of an array: {sum}")