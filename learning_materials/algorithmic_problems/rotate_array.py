# Rotate Array
def rotate(nums, k):
    n = len(nums)
    # To handle cases where k is larger
    # than the length of the array
    k = k % n

    # Reverse the entire array
    reverse(nums, 0, n - 1)
    
    # Reverse the first k elements
    reverse(nums, 0, k - 1)

    # Reverse the remaining elements
    reverse(nums, k, n - 1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1