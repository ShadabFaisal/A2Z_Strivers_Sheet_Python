class Solution:
    # Ceil: Smallest number in array >= X ---> LOWER BOUND
    def ceil_in_sorted_array(self, nums: list[int], n: int, target: int)-> int:
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=low+(high-low)//2
        
            if nums[mid]>=target:
                ans=nums[mid]
                high=mid-1
            else:
                low=mid+1
        
        return ans

        
if __name__ == "__main__":
    nums = [3,6,13,41,56,89,99]
    target=7
    obj = Solution()

    res1=obj.ceil_in_sorted_array(nums, len(nums), target)
    print(f"Ceil of {target} in array is: {res1}")