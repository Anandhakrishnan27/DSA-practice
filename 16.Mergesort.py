class Solution:
    def merge(self, arr, l, m, r):
        # Create temporary arrays
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        i = j = 0
        k = l
        
        # Merge the temp arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left[], if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy remaining elements of right[], if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            m = (l + r) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)

            # Merge the sorted halves
            self.merge(arr, l, m, r)