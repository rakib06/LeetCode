class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        while(temp>0):
            last = temp%10
            rev = rev*10+last
            temp=temp//10
            
        return True if x==rev else False
        
        