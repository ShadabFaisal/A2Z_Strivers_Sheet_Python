class Solution:

    def find_max_consecutive_ones(self, nums: list[int])->int:
        maxi=0
        cnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                maxi=max(maxi,cnt)
            else:
                cnt=0

        return maxi



if __name__ == "__main__":
    nums = [1,1,0,1,1,1,0,1,1]
    
    solution = Solution()
    result = solution.find_max_consecutive_ones(nums)
    print(f"Maximum Consecutive Ones: {result}")