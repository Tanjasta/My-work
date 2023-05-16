def bubbleSort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        for j in range(0, n-i-1):  # Iterate from the first element to the (n-i-1)-th element
            if arr[j] > arr[j+1]:  # Check if the current element is greater than the next element
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # Print the current state of the array after each iteration
        print("Iteration", i+1, ":", arr)

arr = [4, 2, 5, 6, 7, 8]  # Initialize an array

print("Original array:", arr)  # Print the original array

bubbleSort(arr)  # Sort the array using bubble sort

print("Sorted array:", arr)  # Print the sorted array
