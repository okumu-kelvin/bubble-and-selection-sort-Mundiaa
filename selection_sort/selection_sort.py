def selection_sort(arr):
    # TODO: Implement selection sort
    n =len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j #Swap the found minimum element with the first element of the unsorted part
                # This places the smallest element at its correct sorted position

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
my_list = [64, 25, 12, 22, 11, 8]
selection_sort(my_list)
print("Sorted array: ", my_list)

another_list = [5, 3, 8, 4, 2]
selection_sort(another_list)
print("Sorted array: ", another_list)

#Expected Output:
#Sorted array:  [8, 11, 12, 22, 25, 64]
#Sorted array:  [2, 3, 4, 5, 8]