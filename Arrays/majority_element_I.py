class Solution:
    # Moore's Voting Algorithm
    def find_majority_element(self, nums:list[int])->int:
        cnt=0
        element=0
        for num in nums:
            if cnt==0:
                element=num
            if num==element:
                cnt+=1
            else:
                cnt-=1

        cnt1=0
        for num in nums:
            if num==element:
                cnt1+=1

        if cnt1> (len(nums) //2):
            return element
        return -1


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [2,2,3,3,1,2,2]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    element=obj.find_majority_element(arr)
    print(f"Majority Element in the list is: {element}")