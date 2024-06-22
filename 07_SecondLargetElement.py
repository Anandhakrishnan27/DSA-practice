class Solution:
    def print2largest(self, arr, n):
        if n > 1:
            a = sorted(set(arr), reverse=True)  # Remove duplicates
            if len(a) > 1:
                return a[1]  # Return the second largest element
            else:
                return -1  # If all elements are the same
        else:
            return -1  # If there's only one element or the array is empty
