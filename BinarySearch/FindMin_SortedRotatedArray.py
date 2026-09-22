class Solution:

    def checkSortFindMin(self, arr: list[int], left: int, right: int):
        print(left, " ", right)
        if right == (left+1):
            return arr[right]
        mid = (left+right)//2
        if arr[left] < arr[mid]:
            return self.checkSortFindMin(arr, mid, right)
        else:
            return self.checkSortFindMin(arr, left, mid)

    def findMin(self, arr):
        if len(arr) == 1:
            return arr[0]
        if arr[0] < arr[len(arr)-1]:
            return arr[0]
        left = 0
        right = len(arr)-1

        return self.checkSortFindMin(arr, left, right)