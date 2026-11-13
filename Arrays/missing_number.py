class Solution:

    def find_missing_opt1(self, nums: list[int], N: int)->int:
        sum=N*(N+1)/2
        s2=0
        for i in range(len(nums)):
            s2+=nums[i]

        return sum-s2

    def find_missing_opt2(self, nums: list[int], N: int)->int:
            xor1=0
            xor2=0
            for i in range(len(nums)):
                xor2^=nums[i]
                xor1^=(i+1)
            xor1^=N
            
            return xor1^xor2



if __name__ == "__main__":
    nums = [2,3,4,5]
    N=5
    solution = Solution()
    result = solution.find_missing_opt2(nums,N)
    print(int(result))