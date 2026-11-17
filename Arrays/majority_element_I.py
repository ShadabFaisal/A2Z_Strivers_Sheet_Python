


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [4,6,2,5,7,9,1,3]
 
    # Solution object creation
    obj = Solution()
 
    # Result printing
    obj.merge_sort(arr, 0, len(arr)-1)
    print(arr)