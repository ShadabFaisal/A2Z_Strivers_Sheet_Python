class Solution:
    def linear_search(self,nums, n, target)-> int:
        for i in range(n):
            if nums[i]==target:
                return i

        return -1

if __name__ == "__main__":
    nums = [11,2,5,3,4,45]
    target=int(input("Enter the number to be searched: "))
 
    solution = Solution()
    result = solution.linear_search(nums,len(nums), target)
    print(f"The number is present at index {result}!")