class Solution:
    def merge_sort(self, nums:list[int], low:int, high:int):
        # low =0, high=7
        if low>=high:
            return 
        
        mid=low+(high-low)//2
        
        self.merge_sort(nums, low, mid)

        self.merge_sort(nums, mid+1, high)

        self.merge(nums, low, mid, high)

    def merge(self, nums:list[int], low:int,mid:int, high:int):
        ans=[]
        left=low
        right=mid+1

        while left<=mid and right<=high:
            if nums[left]<=nums[right]:
                ans.append(nums[left])
                left+=1
            elif nums[right]<=nums[left]:
                ans.append(nums[right])
                right+=1

        while left<=mid:
            ans.append(nums[left])
            left+=1

        while right<=high:
            ans.append(nums[right])
            right+=1

        for i in range(low, high+1):
            nums[i]=ans[i-low]


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [4,6,2,5,7,9,1,3]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    obj.merge_sort(arr, 0, len(arr)-1)
    print(arr)