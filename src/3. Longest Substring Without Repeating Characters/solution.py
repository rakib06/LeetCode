class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        slength = len(s)
        i = 0  # for count
        j = 0  # for loop
        ans = 0
        while(j < slength):
            if s[j] not in d or i > d[s[j]]:

                d[s[j]] = j
                ans = max(ans, j-i+1)

            else:
                i = d[s[j]] + 1
                ans = max(ans, j-i+1)
                j += -1
            j += 1
        # print(d)
        return ans
