from typing import List

def partition(nums:List[int], l , r) -> int:
    p = l
    pivot = nums[r]
    
    # loop on the range inclusively
    for i in range(l,r+1):
        if nums[i] < pivot:
            #swap
            nums[i], nums[p] = nums[p], nums[i]
            # shift boundary
            p += 1
            
    #swap p with last, this is not a must but needed
    #to shuffle the last element, if another partition is needed
    nums[r], nums[p] = nums[p], nums[r]
    return p

def findKthSmallest(arr, k):
    l, r = 0, len(arr)-1
    targetIndex = k-1
    while l <= r:
        p = partition(arr,l , r)
        # print(arr)
        if targetIndex < p:
            r = p - 1
        elif targetIndex > p:
            l = p + 1
        else:
            return arr[p]

arr, k = [1,7,5,3,2,4,3], 4
print("QuickSelect",findKthSmallest(arr, k))
arr.sort()
print("sorting",arr[k-1])

arr, k = [1,7,5,3,2,4,1,2,0,5,4,3], 6
print("QuickSelect",findKthSmallest(arr, k))
arr.sort()
print("sorting",arr[k-1])

arr, k = [1,7,5,3,2,4,1,2,0,5,4,3,3], 13
print("QuickSelect",findKthSmallest(arr, k))
arr.sort()
print("sorting",arr[k-1])    
        
    