arr = [0, 1, 2, 2, 2, 2, 1, 1, 3, 1, 2, 2, 2]


def bucketSort(arr):
    counts = [0] * len(arr)
    for i in arr:
        counts[i] += 1

    counter = 0
    for i in range(0, len(counts)):
        for j in range(0, counts[i]):
            arr[counter] = i
            counter += 1
    print(arr)


bucketSort(arr)
