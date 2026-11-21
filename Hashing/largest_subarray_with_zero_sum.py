class Solution:
    def largest_subarray_with_zero_sum(self, nums: list[int], n: int) -> int:
        prefix_sum = 0
        first_occurrence = {0: -1}
        longest = 0

        for i in range(n):
            prefix_sum += nums[i]

            if prefix_sum in first_occurrence:
                longest = max(longest, i - first_occurrence.get(prefix_sum))
            else:
                first_occurrence[prefix_sum] = i

        return longest


if __name__ == "__main__":
    nums = [1, -1, 2, -2, 3, -3, 5, 8, -2, 3]
    obj = Solution()
    result = obj.largest_subarray_with_zero_sum(nums, len(nums))
    print(f"Length of largest subarray with zero sum is: {result}")
