class Solution:
    def two_sum(self, nums:list[int], target:int)->list[int]:
        n=len(nums)

        if n<2:
            return []

        value_index_pairs=[(nums[index],index) for index in range(n)]

        value_index_pairs.sort()
        print(value_index_pairs)

        left=0
        right=n-1

        while left<right:
            current_sum=(value_index_pairs[left][0]+value_index_pairs[right][0])

            if current_sum==target:
                return [value_index_pairs[left][1], value_index_pairs[right][1]]
            elif current_sum<target:
                left+=1
            else:
                right-=1

        return []


# Driver code
if __name__ == "__main__":
    
    arr = [2,6,5,8,11]
    target=int(input("Enter target to be checked: "))
 
    obj = Solution()
 
    answer=obj.two_sum(arr, target)
    print(f"The target can be achieved with indexes: {answer}")