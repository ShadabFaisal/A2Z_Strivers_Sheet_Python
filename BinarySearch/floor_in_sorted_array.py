class Solution:
    # Floor: Largest number in array <= X
    def floor_in_sorted_array(self, nums: list[int], n: int, target: int)-> int:
        low=0
        high=n-1
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
        
            if nums[mid]<=target:
                ans=nums[mid]
                low=mid+1
            else:
                high=mid-1
                
        
        return ans

        
if __name__ == "__main__":
    nums = [3,6,13,41,56,89,99]
    target=40
    obj = Solution()

    res1=obj.floor_in_sorted_array(nums, len(nums), target)
    print(f"Floor of {target} in array is: {res1}")