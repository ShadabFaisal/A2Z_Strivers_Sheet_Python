class Solution:
    # Lower Bound - smallest index at which nums[i] >= x
    def search_insert_position(self, nums: list[int], n: int, target: int)-> int:
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=low+(high-low)//2
        
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans

        
if __name__ == "__main__":
    nums = [3,6,13,41,56,89,99]
    target=7
    obj = Solution()

    res1=obj.search_insert_position(nums, len(nums), target)
    print(f"The number can be inserted at index: {res1}")