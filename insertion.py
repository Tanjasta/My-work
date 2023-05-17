def insertionsort(arr):
    for i in range(1, len(arr)):  # Iterate over each element in the array starting from the second element
        key = arr[i]  # Store the current element as the key
        j = i - 1  # Set the initial index of the previous element

        # Move elements of arr[0...i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1  # Decrement the index

        arr[j + 1] = key  # Place the key at its correct position in the sorted subarray
        
        print("List after iteration", i, ":", arr)  # Print the array after each iteration

arr = [4, 2, 5, 6, 7, 8]  # Initialize an array

print("Original array:", arr)  # Print the original array

insertionsort(arr)  # Sort the array using insertion sort

print("Sorted array:", arr)  # Print the sorted array
