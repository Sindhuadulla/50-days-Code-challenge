def rearranging_numbers(arr):
    N = len(arr)
    res = [-1] * N
    arr_set = set(arr)  # Convert list to set for O(1) lookup
    for i in range(N):
        if i in arr_set:
            res[i] = i
    return res

print(rearranging_numbers([-1, -1, 5, 1, 8, 3, 0, -1, 4, -1]))


def rearrangeArray(arr):
    i = 0

    # Iterate through the array
    while i < len(arr):
        # Swap if the element arr[i] is not at arr[arr[i]]
        if arr[i] != -1 and arr[i] != arr[arr[i]]:
            # Swap the elements arr[i] and arr[arr[i]]
            temp = arr[i];
            arr[i]= arr[arr[i]];
            arr[temp]= temp;
             
        else:
            # Increment i if element is at its correct position
            i += 1


# Initialize the array and call the function directly
arr = [-1, -1, 5, 1, 8, 3, 0, -1, 4, -1]

# Call the modifyArray function
rearrangeArray(arr)

# Print the modified array
print(" ".join(map(str, arr)))
