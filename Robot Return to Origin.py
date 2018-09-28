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
    try:
        assert(sol.judgeCircle('UD'))
        assert (sol.judgeCircle(""))
        assert (sol.judgeCircle('UDLRUDLRRL'))
        assert (sol.judgeCircle('LLDD'))

    except (AssertionError):
        print ('Robot did not come to the Origin in the last test case')
