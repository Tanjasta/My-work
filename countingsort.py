def countingsort(array, max_val):
    m = max_val + 1  # Determine the size of the counting array

    count = [0] * m  # Create a counting array initialized with zeros

    for a in array:
        # Count occurrences of each element in array1
        count[a] += 1  # Increment the count for the current element

    i = 0  # Initialize the index for the sorted array

    for a in range(m):  # Iterate over the counting array
        for c in range(count[a]):  # Repeat for the count of each element in the counting array
            array[i] = a  # Assign the element to the sorted array
            i += 1  # Increment the index of the sorted array

    return array

print(countingsort([4, 2, 5, 6, 7, 8], 8))  # Call the countingsort function with the given array and maximum value
