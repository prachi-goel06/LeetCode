class Solution:
    def plusOne(self, digits):
        """
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

        Approach: Start from the last number and move to the front
                if digit is 9 and replace 9 by 0 and take a carry to the next digit on the left

        :type digits: List[int]
        :rtype: List[int]


        """

        carry = False
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] == 9:

                if i == 0:
                    digits[i] = 1
                    digits.append(0)

                    break
                if carry == True:

                    digits[i] = 0
                    carry = True
                else:
                    carry = True
                    digits[i] = 0

            else:
                digits[i] += 1
                break
        print ('result is {}'.format(digits))
        return digits

if __name__ == '__main__':
    sol=Solution()
    print ("testing {} {} {}".format([0],[9,9],[1,2,3]))
    try:
        assert (sol.plusOne([0])==[1])
        assert (sol.plusOne([9,9])==[1,0,0])
        assert (sol.plusOne([1,2,3])==[1,2,4])
    except AssertionError:
        print ("Some test case failed")
