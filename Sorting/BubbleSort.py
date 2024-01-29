def bubble_sort(arr):
    n = len(arr)
    count = 0  # To count the number of swaps

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1

    return count

# Test the function
l1 = [1, 3, 2, 4, 5]
swap_count = bubble_sort(l1)
print("Sorted array:", l1)
print("Number of swaps:", swap_count)
