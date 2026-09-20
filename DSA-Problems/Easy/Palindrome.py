class Solution:
    def isPalindrome(self, x: int):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        num = x
        while num > 0:
            rem = (num%10)
            num = num//10
            rev = (rev * 10) + rem
        if rev == x:
            return True
        else:
            return False