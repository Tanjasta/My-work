import random  # Imports the random module for generating random numbers
import time  # Imports the time module for measuring the execution time
import matplotlib.pyplot as plt  # Imports the matplotlib.pyplot module for creating plots
import pandas as pd  # Imports the pandas module for data manipulation and analysis

def bubblesort(arr):
    n = len(arr)  # Gets the length of the array
    for i in range(n):  # Iterates over each element in the array
        for j in range(0, n-i-1):  # Iterates from the first element to the (n-i-1)-th element
            if arr[j] > arr[j+1]:  # Checks if the current element is greater than the next element
                # Swaps the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionsort(arr):
    n = len(arr)  # Gets the length of the array
    for i in range(n):  # Iterates over each element in the array
        min_idx = i  # Assumes the current index has the minimum element
        
        # Finds the index of the minimum element in the unsorted portion of the array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:  # Compares the current element with the assumed minimum element
                min_idx = j  # Updates the index of the minimum element
        
        # Swaps the current element with the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        

def insertionsort(arr):
    for i in range(1, len(arr)):  # Iterates over each element in the array starting from the second element
        key = arr[i]  # Stores the current element as the key
        j = i - 1  # Sets the initial index of the previous element

        # Moves elements of arr[0...i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shifts elements to the right
            j -= 1  # Decrements the index

        arr[j + 1] = key  # Places the key at its correct position in the sorted subarray

def countingsort(array, max_val):
    m = max_val + 1  # Determines the size of the counting array

    count = [0] * m  # Creates a counting array initialized with zeros

    for a in array:
        # Counts occurrences of each element in array
        count[a] += 1  # Increments the count for the current element

    i = 0  # Initialises the index for the sorted array

    for a in range(m):  # Iterates over the counting array
        for c in range(count[a]):  # Repeats for the count of each element in the counting array
            array[i] = a  # Assigns the element to the sorted array
            i += 1  # Increments the index of the sorted array

    
def mergesort(array):
    print("Splitting ", array)  # Prints a message indicating the current split operation

    if len(array) > 1:  # Checks if there is more than one element in the list
        mid = len(array) // 2  # Calculates the middle index
        lefthalf = array[:mid]  # Divides the list into left half
        righthalf = array[mid:]  # Divides the list into right half

        mergesort(lefthalf)  # Recursively calls mergeSort on the left half
        mergesort(righthalf)  # Recursively calls mergeSort on the right half

        i = 0  # Index for the left half
        j = 0  # Index for the right half
        k = 0  # Index for the original list

        while i < len(lefthalf) and j < len(righthalf):
            # Compares the elements from the left and right halves
            if lefthalf[i] <= righthalf[j]:
                array[k] = lefthalf[i]  # Places the smaller element into the original list
                i += 1
            else:
                array[k] = righthalf[j]  # Places the smaller element into the original list
                j += 1
            k += 1

        while i < len(lefthalf):
            # Copies any remaining elements from the left half to the original list
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            # Copies any remaining elements from the right half to the original list
            array[k] = righthalf[j]
            j += 1
            k += 1


def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]  # Generates a list of random integers between 0 and 1000


# Sorting algorithms

def benchmark_sorting_algorithms():
    algorithms = {
        "Bubble Sort": bubblesort,
        "Selection Sort": selectionsort,
        "Insertion Sort": insertionsort,
        "Counting Sort": countingsort,
        "Merge Sort": mergesort
    }

    input_sizes = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]  # List of input sizes
    results = {algorithm: [] for algorithm in algorithms}  # Creates an empty dictionary to store the results
    output_results = []  # To store the results in the desired format

    for size in input_sizes:
        for algorithm in algorithms:
            arr = generate_random_array(size)  # Generates a random array of the given size
            start_time = time.time()  # Records the start time
            if algorithm == "Counting Sort":
                max_val = max(arr)  # Finds the maximum value in the array
                algorithms[algorithm](arr, max_val)  # Calls the counting sort algorithm with the maximum value
            else:
                algorithms[algorithm](arr)  # Calls the sorting algorithm
            end_time = time.time()  # Records the end time
            total_time = (end_time - start_time) * 1000  # Calculates the total execution time in milliseconds
            avg_time = total_time / 10.0  # Calculates the average execution time over 10 iterations
            results[algorithm].append(avg_time)  # Adds the average time to the results dictionary

    # Stores the results in the desired format
    for algorithm in algorithms:
        output_results.append([f"{algorithm}"] + [f"{time:.3f}" for time in results[algorithm]])

    # Prints the results
    columns = ["Algorithm"] + [str(size) for size in input_sizes]
    df = pd.DataFrame(output_results, columns=columns)
    print(df.to_string(index=False))  # Print the DataFrame without the index

    # Plots the results
    fig, ax = plt.subplots()
    ax.set_title("Sorting Algorithms Benchmarking")
    ax.set_xlabel("Input Size (n)")
    ax.set_ylabel("Running Time (milliseconds)")

    for algorithm in algorithms:
        ax.plot(input_sizes, results[algorithm], label=algorithm)  # Plot the running time for each algorithm

    ax.legend()  # Shows the legend
    plt.savefig('sorting_algorithms.png')  # Saves the plot to a file
    plt.show()  # Displays the plot


benchmark_sorting_algorithms()  # Runs the benchmarking function
