
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        if A==[1]: #edge cases
            return [0]
        elif A==[0]: #edge cases
            return [1]

        else:
            new_list=[[abs(j-1) for j in i[::-1]] for i in A]

        print (new_list)
        return (new_list)

if __name__ == '__main__':
    sol=Solution()
    assert(sol.flipAndInvertImage([[0,1,0,1],[0,0,0],[1,1,1,1]])==[[0, 1, 0, 1], [1, 1, 1], [0, 0, 0, 0]])
    assert (sol.flipAndInvertImage([[1],[0]]) == [[0],[1]])
