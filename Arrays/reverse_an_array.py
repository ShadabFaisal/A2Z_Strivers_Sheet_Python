class Solution:
    def reverse_an_array(self, nums:list[int])->list[int]:
       start=0
       end=len(nums)-1
       while start<=end:
           temp=nums[start]
           nums[start]=nums[end]
           nums[end]=temp
           start+=1
           end-=1

if __name__=="__main__":
    nums=[1,2,3,4,5]

    solution=Solution()
    solution.reverse_an_array(nums)
    print(nums)