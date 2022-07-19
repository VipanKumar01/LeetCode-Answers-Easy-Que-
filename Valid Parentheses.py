# Name = Vipan Kumar
# GitHub user name = @VipanKumar01


class Solution:
    def isValid(self, s: str) -> bool:
        CheckParenth = {'(':')', '{':'}', '[':']'}
        openParenth = ['(', '[', '{']
        stk = []
        if s[0] not in CheckParenth:
            return False
            
# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

        for i in s:
            if i in openParenth:
                stk.append(i)
            elif len(stk) != 0 and i == CheckParenth[stk[-1]]:
                stk.pop()
            else:
                return False
            
        if stk == []:
            return True
        else:
            return False
           
# -- Happy Code --
