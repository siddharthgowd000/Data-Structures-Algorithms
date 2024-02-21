def merge(arr,l,mid,r):
    left = l
    right = mid+1
    temp = []

    while left<=mid and right<=r:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left<=mid:
        temp.append(arr[left])
        left += 1
    while right<= r:
        temp.append(arr[right])
        right += 1
    for i in range(r+1):
        arr[i] = temp[i-1]


def mergeSort(arr, l, r):
    # Write Your Code Here
    if l>=r:
        return
    mid = (l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)
arr = [2,5,4,3,1,6]
mergeSort(arr,0,5)
print(arr)

