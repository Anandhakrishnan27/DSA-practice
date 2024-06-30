class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # Create a list to store the frequency of each element
        freq_list = [0] * N
     
        # Count the frequency of each element in the array
        for num in arr:
            if num <= N:
                freq_list[num-1] += 1
        
        # Update the original array with the frequency of each element
        arr[:N] = freq_list
        
        return arr
