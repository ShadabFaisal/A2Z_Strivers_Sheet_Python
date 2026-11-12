class Solution:
    def union_of_two_sorted_array(self,nums1: list[int], nums2: list[int])-> list[int]:
        n=len(nums1)
        m=len(nums2)

        union_list = []
        i=0
        j=0
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                current=nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                current=nums2[j]
                j+=1
            else:
                current=nums1[i]
                i+=1
                j+=1
            if not union_list or union_list[-1]!=current:
                union_list.append(current)

        while i<n:
            if not union_list or union_list[-1]!=nums1[i]:
                union_list.append(nums1[i])
            i+=1

        while j<m:
            if not union_list or union_list[-1]!=nums2[j]:
                union_list.append(nums2[j])
            j+=1

        return union_list


if __name__ == "__main__":
    nums1 = [1, 1, 2, 3, 4]
    nums2 = [2, 3, 5, 6,12]
 
    solution = Solution()
    result = solution.union_of_two_sorted_array(nums1, nums2)
    print(f"Union of two sorted array: {result}")