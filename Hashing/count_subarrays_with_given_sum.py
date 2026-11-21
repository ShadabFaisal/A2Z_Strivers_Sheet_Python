class Solution:
    def count_subarrays_with_given_sum(slef,nums:list[int], n:int, k : int)-> int:
        
        prefix_sum = 0
        cnt=0
        prefix_count= {0: 1}
        
        for i in range(n):
            prefix_sum += nums[i]
            remove=prefix_sum-k
            
            cnt+=prefix_count.get(remove,0)
            prefix_count[prefix_sum] = (prefix_count.get(prefix_sum,0)) + 1
        
        return cnt



if __name__ == "__main__":
    nums = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    target=3
    obj = Solution()
    result = obj.count_subarrays_with_given_sum(nums, len(nums), target)
    print(f"Count of subarrays with sum k is: {result}")