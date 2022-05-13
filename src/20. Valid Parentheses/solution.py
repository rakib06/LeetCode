class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{', }
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []
        i = 0
        l = len(s)
        while(i < l):
            # print(stack)
            if s[i] in opening:
                stack.append(s[i])

            elif s[i] in closing:
                if not stack:
                    return False
                # elif s[i] not in stack:
                #     stack.append(s[i])
                elif stack[-1] == d[s[i]]:

                    # print("before pop:", stack, " s[i]= ", s[i])
                    stack.pop()
                    # print("after pop:", stack)
                elif s[i] not in stack:
                    return False

            i += 1
            # print(i)

        if not stack:
            return True
        else:
            return False


print(Solution().isValid('()') == True)
print(Solution().isValid('()[]{}') == True)
print(Solution().isValid('(]') == False)
print(Solution().isValid('[({})]()') == True)
print(Solution().isValid("[(){}{]") == False)
print(Solution().isValid("[(){}]") == True)
print(Solution().isValid("{[]}") == True)
print(Solution().isValid("(])") == False)
