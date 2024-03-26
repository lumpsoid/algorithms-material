def bubble_sort(arr: list) -> list:
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the
    a worst-case and average complexity of O(n^2)

    Args:
        arr (list): list of integers

    Returns:
        list: list of integers in ascending order
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr