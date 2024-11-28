#Binary Search Implementation

import random

def binary_search(arr, target, left=None, right=None, find_first=True):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    # Base case
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
         #Find first occurence
         if find_first:
            if mid == left or arr[mid-1] < target:
                return mid
            return binary_search(left, mid - 1)
        # Find Last occurence
         else:
            if mid == right or arr[mid+1] > target:
                return mid
            return binary_search(mid + 1, right)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


if __name__ == "__main__":
    arr = sorted([random.randint(1, 20) for _ in range(20)])
    
    search_values = random.sample(arr, min(5, len(arr))) # select random search values from the array
    
    print("Random Array:", arr)
    print("Random Search Values: ", search_values) 

    print("Binary Search:")
    for value in search_values:
        index = binary_search(arr, value)
        print(f"Target {value}: Index {index}")