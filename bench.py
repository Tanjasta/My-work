import random
import time
import matplotlib.pyplot as plt

def bubblesort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        for j in range(0, n-i-1):  # Iterate from the first element to the (n-i-1)-th element
            if arr[j] > arr[j+1]:  # Check if the current element is greater than the next element
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionsort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        min_idx = i  # Assume the current index has the minimum element
        
        # Find the index of the minimum element in the unsorted portion of the array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:  # Compare the current element with the assumed minimum element
                min_idx = j  # Update the index of the minimum element
        
        # Swap the current element with the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        

def insertionsort(arr):
    for i in range(1, len(arr)):  # Iterate over each element in the array starting from the second element
        key = arr[i]  # Store the current element as the key
        j = i - 1  # Set the initial index of the previous element

        # Move elements of arr[0...i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1  # Decrement the index

        arr[j + 1] = key  # Place the key at its correct position in the sorted subarray

def countingsort(array, max_val):
    m = max_val + 1  # Determine the size of the counting array

    count = [0] * m  # Create a counting array initialized with zeros

    for a in array:
        # Count occurrences of each element in array
        count[a] += 1  # Increment the count for the current element

    i = 0  # Initialize the index for the sorted array

    for a in range(m):  # Iterate over the counting array
        for c in range(count[a]):  # Repeat for the count of each element in the counting array
            array[i] = a  # Assign the element to the sorted array
            i += 1  # Increment the index of the sorted array

    
def mergesort(array):
    print("Splitting ", array)  # Print a message indicating the current split operation

    if len(array) > 1:  # Check if there is more than one element in the list
        mid = len(array) // 2  # Calculate the middle index
        lefthalf = array[:mid]  # Divide the list into left half
        righthalf = array[mid:]  # Divide the list into right half

        mergesort(lefthalf)  # Recursively call mergeSort on the left half
        mergesort(righthalf)  # Recursively call mergeSort on the right half

        i = 0  # Index for the left half
        j = 0  # Index for the right half
        k = 0  # Index for the original list

        while i < len(lefthalf) and j < len(righthalf):
            # Compare the elements from the left and right halves
            if lefthalf[i] <= righthalf[j]:
                array[k] = lefthalf[i]  # Place the smaller element into the original list
                i += 1
            else:
                array[k] = righthalf[j]  # Place the smaller element into the original list
                j += 1
            k += 1

        while i < len(lefthalf):
            # Copy any remaining elements from the left half to the original list
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            # Copy any remaining elements from the right half to the original list
            array[k] = righthalf[j]
            j += 1
            k += 1


def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

def benchmark_sorting_algorithms():
    algorithms = {
        "Bubble Sort": bubblesort,
        "Selection Sort": selectionsort,
        "Insertion Sort": insertionsort,
        "Counting Sort": countingsort,
        "Merge Sort": mergesort
    }

    input_sizes = [10, 100, 500, 1000, 5000, 10000]
    results = {algorithm: [] for algorithm in algorithms}

    for size in input_sizes:
        for algorithm in algorithms:
            arr = generate_random_array(size)
            start_time = time.time()
            algorithms[algorithm](arr)
            end_time = time.time()
            total_time = (end_time - start_time) * 1000  # Convert to milliseconds
            avg_time = total_time / 10.0
            results[algorithm].append(avg_time)
            print(f"{algorithm} with {size} elements: {avg_time:.6f} milliseconds")

    # Plot the results
    fig, ax = plt.subplots()
    ax.set_title("Sorting Algorithms Benchmarking")
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Running Time (milliseconds)")

    for algorithm in algorithms:
        ax.plot(input_sizes, results[algorithm], label=algorithm)

    ax.legend()
    plt.show()



