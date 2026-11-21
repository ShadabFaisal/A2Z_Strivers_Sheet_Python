class Solution:
    def binary_search(self, nums: list[int], n: int, target: int)-> int:
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1

        return -1
    
    def recursive_binary_search(self, nums:list[int], low:int, high:int, target:int)->int:
        if low>high:
            return -1
        
        mid=low+(high-low)//2
        
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            self.recursive_binary_search(nums, low, mid-1, target)
            
        return self.recursive_binary_search(nums, mid+1, high, target)

        
if __name__ == "__main__":
    nums = [3,6,13,41,56,89,99]
    target=99
    obj = Solution()

    res1=obj.binary_search(nums, len(nums), target)
    res2=obj.recursive_binary_search(nums, 0, len(nums)-1, target)

    print(f"The target is present at index: {res1}")
    print(f"The target is present at index: {res2}")
