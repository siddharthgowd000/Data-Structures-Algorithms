def quickSort(arr,low,high):
    if low < high:
        pivot = arr[low]
        left = low + 1
        right = high

        while left <= right:

            while left <= right and arr[left] <= pivot :
                left += 1
            
            while left <= right and arr[right] > pivot:
                right -= 1

            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
    
    
        arr[low], arr[right] = arr[right], arr[low]
        
        quickSort(arr,low,right-1)
        quickSort(arr,right+1,high)

    

arr = [29, 9, 24, 14, 19, 27]
quickSort(arr,0,len(arr)-1)
print(arr)
