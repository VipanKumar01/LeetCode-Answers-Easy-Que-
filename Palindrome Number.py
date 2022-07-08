# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        d = 0
        s = 0
        
        while x > 0:
            d = x%10
            s = s*10+d
            x = x//10
            
        if temp == s:
            return True
        else:
            return False

# --HappyCode--
