def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    n = len(unsorted_list)
    for i in range(n):
        swapped = False
        # Inner loop for comparisons and swaps within each pass

        for j in range(0, n - i - 1):
            # The -i-1 ensures that already sorted elements at the end are not re-compared
            # Compare adjacent elements
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap if elements are in the wrong order
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

    #If no swaps occurred in the inner loop, the array is sorted
        if not swapped:
            break
    return unsorted_list

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
sorted_list = bubble_sort(my_list)
print("Sorted list (ascending):", sorted_list)

#Expected output:
#Original list: [64, 34, 25, 12, 22, 11, 90]
#Sorted list (ascending): [11, 12, 22, 25, 34, 64, 90]
