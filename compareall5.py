import random
import timeit
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1
    i = 0
    for j in range(max_value + 1):
        while count[j] > 0:
            arr[i] = j
            i += 1
            count[j] -= 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

def benchmark_sorting_algorithms():
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Counting Sort": counting_sort,
        "Merge Sort": merge_sort
    }
    
    input_sizes = [10, 100, 500, 1000, 5000, 10000]
    results = {algorithm: [] for algorithm in algorithms}
    
    for size in input_sizes:
        arr = generate_random_array(size)
        for algorithm in algorithms:
            total_time = timeit.timeit(lambda: algorithms[algorithm](arr.copy()), number=10)
            avg_time = total_time / 10.0
            results[algorithm].append(avg_time)
            print(f"{algorithm} with {size} elements: {avg_time:.6f} seconds")
    
    # Plot the results
    fig, ax = plt.subplots()
    ax.set_title("Sorting Algorithms Benchmarking")
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Running Time (seconds)")
    
    for algorithm in algorithms:
        ax.plot(input_sizes, results[algorithm], label=algorithm)
    
    ax.legend()
    plt.show()
