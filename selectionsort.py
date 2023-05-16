#Selection sort in Python, sorting by finding min_index

def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Iterate over each element in the array
        min_idx = i  # Assume the current index has the minimum element
        
        # Find the index of the minimum element in the unsorted portion of the array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:  # Compare the current element with the assumed minimum element
                min_idx = j  # Update the index of the minimum element
        
        # Swap the current element with the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Print the array after each iteration
        print(arr)

arr = [4, 2, 5, 6, 7, 8]  # Initialize an array

print("Original array:", arr)  # Print the original array

print("Selection sort diagram:")  # Print a label for the diagram

selection_sort(arr)  # Sort the array using selection sort

print("Sorted array:", arr)  # Print the sorted array
