class Solution:

    count = 0

    def merge(self, res: list[int], left: list[int], right: list[int]):
        
        idx = 0
        lidx = 0
        ridx = 0
        while lidx < len(left) and ridx < len(right):
            if left[lidx] <= right[ridx]:
                res.append(left[lidx])
                lidx += 1
            else:
                res.append(right[ridx])
                ridx += 1
                self.count += len(left)-lidx
        
        while lidx < len(left):
            res.append(left[lidx])
            lidx += 1
        
        while ridx < len(right):
            res.append(right[ridx])
            ridx += 1
        
        return res

    def divideAndMerge(self, nums: list[int], start: int, end: int) -> list[int]:
        res = list()
        if start==end:
             res.append(nums[start])
        elif start>end:
            return res
        else:

            mid = (start+end)//2
            left = self.divideAndMerge(nums, start, mid)
            right = self.divideAndMerge(nums, mid+1, end)

            res = self.merge(res, left, right)
        
        return res
        

    def numberOfInversions(self, nums):
        res = self.divideAndMerge(nums, 0, len(nums)-1)
        return self.count