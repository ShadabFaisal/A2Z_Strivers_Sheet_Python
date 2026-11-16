class Solution:
    def find_count_of_odd_nums(self, nums:list[int])->int:
        cnt=0
        for i in range(len(nums)):
            if nums[i]%2==1:
                cnt+=1

        return cnt



if __name__=="__main__":
    nums=[1,22,31,4,5,16]

    solution=Solution()
    count=solution.find_count_of_odd_nums(nums)
    print(f"Count of Odd elements in an array: {count}")