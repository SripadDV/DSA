class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        m1 = 0
        count1 = 0
        m2 = 0
        count2 = 0
        for i in nums:
            if count1 == 0:
                m1 = i
                count1 = 1
            elif i == m1:
                count1 += 1
            elif count2 == 0:
                m2 = i
                count2 = 1
            elif i == m2:
                count2 += 1
                if count2 > count1:
                    tempm1 = m1
                    m1 = m2
                    m2 = tempm1

                    tempc1 = count1
                    count1 = count2
                    count2 = tempc1
            else:
                count1 -= 1
                count2 -= 1
        
        res = list()
        count1 = 0
        count2 = 0
        for i in nums:
            if i == m1:
                count1 += 1
            elif i == m2:
                count2 += 1
            else:
                pass

        if count1>len(nums)//3:
            res.append(m1)
        if count2>len(nums)//3:
            res.append(m2)
        return res