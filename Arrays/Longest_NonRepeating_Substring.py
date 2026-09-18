class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curLen = 0
        maxLen = 0
        charSet = set()

        left = 0
        right = 0
        while right < len(s):
            if s[right] in charSet:
                while s[left] != s[right]:
                    charSet.remove(s[left])
                    left += 1
                left += 1
            
            charSet.add(s[right])
            maxLen = max(maxLen, right-left+1)
            right += 1
        return maxLen