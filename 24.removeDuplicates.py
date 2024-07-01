class Solution:
    def remove_duplicate(self, A, N):
        if N == 0:
            return 0
        
        # Initialize two pointers
        i = 0  # Pointer for iterating through the array
        j = 1  # Pointer for placing unique elements
        
        # Iterate through the array
        while i < N - 1:
            if A[i] != A[i + 1]:
                # Found a unique element
                A[j] = A[i + 1]
                j += 1
            i += 1
        
        # Return the count of unique elements
        return j