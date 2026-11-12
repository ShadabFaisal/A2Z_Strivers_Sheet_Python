class Solution:
    def intersection_of_two_sorted_array(self,nums1: list[int], nums2: list[int])-> list[int]:
        n=len(nums1)
        m=len(nums2)

        intersection_list = []
        i=0
        j=0
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                intersection_list.append(nums1[i])
                i+=1
                j+=1

        return intersection_list


if __name__ == "__main__":
    nums1 = [1, 1, 2, 3, 4]
    nums2 = [2, 3, 4, 5, 6]
 
    solution = Solution()
    result = solution.intersection_of_two_sorted_array(nums1, nums2)
    print(f"Intersection of two sorted array: {result}")