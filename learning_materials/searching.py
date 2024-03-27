from abc import ABC, abstractmethod
from typing import List

class Searching(ABC):
  @abstractmethod
  def search(self, arr: List[int], x: int) -> int:
    pass

  @classmethod
  def search_test(cls):
    arr = [1,2,3,4,5]
    x = 3
    instance = cls()
    index = instance.search(arr, x)
    try:
      assert(arr[index] == x)
      print("OK")
    except:
      print(f"{arr[index]} != {x}")
      print('Failed')

class BinarySearch(Searching):
  """_summary_

  Args:
      Searching (_type_): _description_
  """
  def search(self, arr: List[int], x: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class InterpolationSearch(Searching):
  """_summary_

  Args:
      Searching (_type_): _description_
  """
  def search(self, arr: List[int], x: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + int(float(high - low) / (arr[high] - arr[low] * (x - arr[low])))
        if arr[pos] == x:
          return pos 
        if x < arr[pos]:
          high = pos - 1
        else:
          low = pos + 1
    return -1