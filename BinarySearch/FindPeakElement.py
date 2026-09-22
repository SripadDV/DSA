class Solution:
    def findPeakElement(self, arr):
        
        if len(arr) == 1:
            return 0

        if arr[0] > arr[1]:
            return 0
        if arr[len(arr)-2]<arr[len(arr)-1]:
            return len(arr)-1

        for i in range(1, len(arr)-1):
            if (arr[i-1] < arr[i]) and (arr[i+1] < arr[i]):
                return i
        
        return -1