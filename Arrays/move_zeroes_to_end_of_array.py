class Solution:
    def move_zeroes_to_end(self,nums,n):
        j=-1
        for i in range(n):
            if nums[i] == 0:
                j=i
                break

        if j==-1:
            return

        for i in range(j,n):
            if nums[i] != 0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j += 1

if __name__ == "__main__":
    nums = [1,0,0,2,5,2,3,4,5]
 
    solution = Solution()
    solution.move_zeroes_to_end(nums,len(nums))
    print(nums)