class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = sorted([len(item) for item in strs])
        temp = ''
        flag = 1

        for i in range(0, length[0]):
            if flag == 1:
                temp = strs[0][0:i+1]
                for item in strs:
                    if item[:i+1] == temp and flag == 1:
                        flag = 1
                        # print("--------> temp= ", temp," item--", item[:i+1])
                    else:
                        flag = 0
                        temp = temp[:-1]
                        break
            else:
                break
        return temp
