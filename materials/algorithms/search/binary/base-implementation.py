def binary_search(arr: list, x: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return x
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1