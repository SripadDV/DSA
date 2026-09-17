class Solution:

    count = 0

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        
        res = list()
        lidx, ridx = 0, 0
        l, r = 0, 0
        while l<len(left) and r<len(right):
            if left[l] > 2*right[r]:
                self.count += len(left)-l
                r += 1
            else:
                l += 1

        while lidx < len(left) and ridx < len(right):
            if left[lidx] <= right[ridx]:
                res.append(left[lidx])
                lidx += 1
            else:
                res.append(right[ridx])
                ridx += 1
        
        while lidx < len(left):
            res.append(left[lidx])
            lidx += 1
        while ridx <len(right):
            res.append(right[ridx])
            ridx += 1
        
        return res

    def getReversePairCount(self, nums: list[int], start: int, end: int) -> list[int]:
        
        res = list()
        if start==end:
            res.append(nums[start])
            # print("Return ", res)
            return res
        
        left = self.getReversePairCount(nums, start, (start+end)//2)
        right = self.getReversePairCount(nums, (start+end)//2+1, end)
        # print(left)
        # print(right)
        return self.merge(left, right)


    def reversePairs(self, nums: list[int]) -> int:
        res = self.getReversePairCount(nums, 0, len(nums)-1)
        return self.count
        