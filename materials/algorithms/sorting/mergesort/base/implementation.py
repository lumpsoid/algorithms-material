def merge_sort(arr: list[int]):
  """Merge sort
  In the worst case, merge sort uses approximately 39% fewer comparisons than quicksort does in its average case, and in terms of moves, merge sort's worst case complexity is O(n log n) - the same complexity as quicksort's best case.

  Args:
      arr (_type_): _description_
  """
  if len(arr) <= 1:
      return arr

  # Split the array into two halves
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  # Recursively sort each half
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  # Merge the sorted halves
  return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Compare elements from both arrays and add the smaller one to the result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right arrays
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

# Example usage:
arr = [5, 9, 1, 3, 4, 6, 6, 3, 2]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
