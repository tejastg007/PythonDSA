def quickSort(arr, start, end):
    if end <= start:
        return
    pivot = arr[end]
    left = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    arr[end], arr[left] = arr[left], arr[end]
    quickSort(arr, start, left-1)
    quickSort(arr, left+1, end)


arr = [8, 1, 2, 3, 6, 9, 1]
quickSort(arr, 0, len(arr)-1)
print(arr)
