class Solution:
    def reverse(self,nums,start,end):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1

    def left_rotate_by_d_place(self, nums, d):
        n=len(nums)
        d=d%n
        self.reverse(nums,0,d-1)
        self.reverse(nums,d,n-1)
        self.reverse(nums,0,n-1)
  

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    d=int(input("Enter the number of places to rotate: "))
 
    solution = Solution()
    solution.left_rotate_by_d_place(nums,d)
    print(nums)