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

    print("Merging ", array)  # Print a message indicating the current merge operation

array = [4, 2, 5, 6, 7, 8]
mergesort(array)  # Call the mergeSort function
print(array)  # Print the sorted list
