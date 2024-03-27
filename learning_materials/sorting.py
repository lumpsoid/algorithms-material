from abc import ABC, abstractmethod
from typing import List


class Sorting(ABC):
    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        pass

    @classmethod
    def test_sort(cls):
        arr = [4, 3, 2, 1]
        print("initial arr:", arr)
        instance = cls()
        instance.sort(arr)
        try:
            assert(arr == [1,2,3,4])
            print("OK")
        except:
            print(arr)
            print("Failed")

class SortTester:
    @staticmethod
    def test_sort(sorting_class: Sorting):
        arr = [4, 3, 2, 1]
        sorting = sorting_class()
        sorting.sort(arr)
        try:
            assert(arr == [1,2,3,4])
            print("OK")
        except:
            print(arr)
            print("Failed")


class BubbleSort(Sorting):
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the
    a worst-case and average complexity of O(n^2)

    Args:
        arr (list): list of integers

    Returns:
        list: list of integers in ascending order
    """

    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class BubbleSortOptimized(Sorting):
    @abstractmethod
    def sort(self, arr: list[int]):
        n = len(arr)
        while n > 1:
            newn = 0
            for i in range(1, n):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    newn = i
            n = newn
        return arr


class InsertionSort(Sorting):
    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


class MergeSort(Sorting):
    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
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
        left_half = self.sort(left_half)
        right_half = self.sort(right_half)

        # Merge the sorted halves
        return self.merge(left_half, right_half)

    @abstractmethod
    def merge(self, left, right):
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


class QuickSort(Sorting):
    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class SelectionSort(Sorting):
    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


class TimSort(Sorting):
    @abstractmethod
    def sort(self, arr: List[int]) -> List[int]:
        min_run = 32
        n = len(arr)

        for i in range(0, n, min_run):
            self.insertion_sort(arr, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))

                merged_array = self.merge(
                    left=arr[start : midpoint + 1], right=arr[midpoint + 1 : end + 1]
                )

                arr[start : start + len(merged_array)] = merged_array

            size *= 2

        return arr

    @abstractmethod
    def insertion_sort(self, arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1

        for i in range(left + 1, right + 1):
            key_item = arr[i]
            j = i - 1
            while j >= left and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item

        return arr

    @abstractmethod
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left[0] < right[0]:
            return [left[0]] + self.merge(left[1:], right)
        return [right[0]] + self.merge(left, right[1:])
