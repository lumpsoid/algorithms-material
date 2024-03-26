def buble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    while n > 1:
        newn = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                newn = i
        n = newn
    return arr