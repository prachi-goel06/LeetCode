class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        new_list = [B.index(i) for i in A]
        print (new_list)

if __name__ == '__main__':
    instance=Solution()
    instance.anagramMappings([0,32,45,67,89],[89,45,0,67,32])