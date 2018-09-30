class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (len(nums)):
            j=nums[i]
            while nums[i]!=-1 and (j!=-1) and j-1!=-1 :
                temp=nums[j-1]
                nums[i]=0
                nums[j-1]=-1
                j=temp
            #print ("i is {} j is {} nums{}".format(i,j,nums))
        return [i+1 for i in range (len(nums)) if nums[i]==0]

if __name__ == '__main__':
    sol=Solution()
    try:
        assert (sol.findDisappearedNumbers([1,1,2,2])==[3,4])
    except (AssertionError):
        print ('Solution is not true')
