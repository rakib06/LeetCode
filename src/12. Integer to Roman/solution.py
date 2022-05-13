class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def len(L):
            i = 0
            for item in L:
                i += 1
            return i

        sum = []
        carry = 0
        dif = len(l1)-len(l2)
        if dif > 0:
            # l2 = l2[::-1]
            for i in range(dif):
                l2.append(0)
            # l2 = l2[::-1]
            # print('L2---',l2)
        if dif < 0:
            # l1 = l1[::-1]
            for i in range(abs(dif)):
                l1.append(0)
            # l1 = l1[::-1]
            # print('l1---',l1)
        # while(l1.next!=0):
        # print(l1, l2, type(l1) )
        for i in range(len(l1)):
            # sum.val = (l1[i]+l2[i])%10+carry
            t = (l1[i]+l2[i]+carry) % 10
            # print("--->", t, l1[i], l2[i], carry )
            sum.append(t)
            carry = (l1[i]+l2[i]+carry)//10
        if carry != 0:
            sum.append(carry)
        return sum
