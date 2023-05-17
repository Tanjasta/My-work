# Code for merge sort
# Merges two subarrays within the given arr[] array
# The first subarray spans from index l to m
# The second subarray spans from index m+1 to r

def merge(arr, l, m, r):
    n1 = m - l + 1  # Calculate the size of the left subarray
    n2 = r - m     # Calculate the size of the right subarray

    # create temp arrays
    L = [0] * (n1)  # Create a temporary array for the left subarray
    R = [0] * (n2)  # Create a temporary array for the right subarray

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]  # Copy elements from the original array to the left subarray

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]  # Copy elements from the original array to the right subarray

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of the first subarray (left subarray)
    j = 0     # Initial index of the second subarray (right subarray)
    k = l     # Initial index of the merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]  # If the current element in the left subarray is smaller or equal, put it in the merged array
            i += 1
        else:
            arr[k] = R[j]  # If the current element in the right subarray is smaller, put it in the merged array
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]  # Copy the remaining elements from the left subarray to the merged array
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]  # Copy the remaining elements from the right subarray to the merged array
        j += 1
        k += 1

# l is for the left index and r is the right index of the sub-array of arr to be sorted
 
def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l+(r-l)//2  # Calculate the middle index to divide the array into two halves
 
        # Sort first and second halves recursively
        mergeSort(arr, l, m)  # Sort the left half of the array
        mergeSort(arr, m+1, r)  # Sort the right half of the array
        merge(arr, l, m, r)  # Merge the two sorted halves
 
 
# Driver code to test the above functions
arr = [4, 2, 5, 6, 7, 8]
n = len(arr)
print("Original array")
for i in range(n):
    print("%d" % arr[i], end=" ")
 
mergeSort(arr, 0, n-1)  # Call the mergeSort function to sort the array
print("\n\nSorted array")
for i in range(n):
    print("%d" % arr[i], end=" ")
