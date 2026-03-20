# Python program for implementation of Insertion Sort


# Function to do insertion sort
def insertion_sort(array_to_sort):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array_to_sort)):

        key = array_to_sort[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array_to_sort[j]:
            array_to_sort[j + 1] = array_to_sort[j]
            j -= 1

        array_to_sort[j + 1] = key


if __name__ == '__main__':
    # Driver code to test above

    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    for a in range(len(arr)):
        print("%d " % arr[a], end='')

    print()

    # This code is contributed by Mohit Kumra
