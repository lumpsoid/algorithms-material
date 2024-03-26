def bidirectional_bubble_sort(arr: list[int]) -> list[int]:
  """Bidirectional Bubble Sort

  used primarily as an educational tool
  Typically cocktail sort is less than two times faster than bubble sort. 
  Worst-case performance:	O(n^2)
  Best-case performance:	O(n)

  Args:
      arr (list[int]): _description_

  Returns:
      list[int]: _description_
  """
  n = len(arr)
  left = 0
  right = n - 1
  while left < right:
      for i in range(left, right):
          if arr[i] > arr[i + 1]:
              arr[i], arr[i + 1] = arr[i + 1], arr[i]
      right -= 1
      for i in range(right, left, -1):
          if arr[i - 1] > arr[i]:
              arr[i - 1], arr[i] = arr[i], arr[i - 1]
      left += 1
  return arr