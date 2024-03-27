from typing import List

def containsDuplicate(nums: List[int]) -> bool:
  dup = set(nums)
  
  if len(dup) == len(nums):
    return False
  return True

def containsDuplicateLoop(nums: List[int]) -> bool:
  dup = set()
  
  for num in nums:
    if num in dup:
      return True
    dup.add(num)
  return False