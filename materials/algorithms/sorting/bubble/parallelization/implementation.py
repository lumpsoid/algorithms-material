import multiprocessing

def bubble_sort_parallel(num_processes: int , arr: list[int]) -> list[int]:
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(arr) // num_processes
    
    # Function for parallel bubble sort
    def bubble_sort_chunk(chunk):
        for i in range(len(chunk)):
            for j in range(len(chunk) - 1):
                if chunk[j] > chunk[j + 1]:
                    chunk[j], chunk[j + 1] = chunk[j + 1], chunk[j]
        return chunk
    
    # Split the array into chunks and sort each chunk in parallel
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(bubble_sort_chunk, chunks)
    
    # Merge sorted chunks
    sorted_arr = []
    for chunk in sorted_chunks:
        sorted_arr.extend(chunk)
    
    # Perform one final pass of bubble sort to ensure correct ordering
    for i in range(len(sorted_arr)):
        for j in range(len(sorted_arr) - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    
    return sorted_arr

# Example usage:
arr = [5, 9, 1, 3, 4, 6, 6, 3, 2]
print("Original array:", arr)
sorted_arr = bubble_sort_parallel(arr)
print("Sorted array:", sorted_arr)
