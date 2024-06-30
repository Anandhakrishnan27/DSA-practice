def frequencyCount(arr, N):
    freq_dict = {}
    
    # Count the frequency of each element in the array
    for num in arr:
        if num <= N:
            freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Update the original array with the frequency of each element
    for i in range(1, N+1):
        arr[i-1] = freq_dict.get(i, 0)
    
    return arr