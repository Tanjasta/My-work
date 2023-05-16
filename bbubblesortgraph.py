import matplotlib.pyplot as plt

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # Plot the current state of the array after each iteration
        plt.plot(arr)
        plt.pause(0.1)
    # Show the final sorted array plot
    plt.plot(arr)
    plt.show()

arr = [4, 2, 5, 6, 7, 8]

print("Original array:", arr)

bubbleSort(arr)

print("Sorted array:", arr)