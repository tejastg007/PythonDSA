def merge(arr, start, end):

    if (end <= start):
        return arr
    mid = (start+end)//2
    merge(arr, start, mid)
    merge(arr, mid+1, end)
    mergeArrays(arr, start, end, mid)
    return arr


def mergeArrays(arr, start, end, mid):
    # make copy of left array
    leftArray = arr[start:mid+1]
    # make copy of right array
    rightArray = arr[mid+1:end+1]

    i = j = 0  # indices for left and right array
    arrIndex = start  # index for actual array

    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            arr[arrIndex] = leftArray[i]
            i += 1
        else:
            arr[arrIndex] = rightArray[j]
            j += 1
        arrIndex += 1

    while i < len(leftArray):
        arr[arrIndex] = leftArray[i]
        i += 1
        arrIndex += 1

    while j < len(rightArray):
        arr[arrIndex] = rightArray[j]
        j += 1
        arrIndex += 1


arr = [1, 10, 5, 4, 3]
ans = merge(arr, 0, len(arr)-1)
print(ans)
