class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if (moves.count('U')==moves.count('D') and moves.count ('L')==moves.count('R')):
            return True
        else:
            return False

if __name__ == '__main__':
    sol=Solution()
    assert(sol.judgeCircle('UD')==True)
    assert (sol.judgeCircle("")==True)
    assert (sol.judgeCircle('UDLRUDLRRL')==True)
    assert (sol.judgeCircle('LLDD')==False)

