class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = list(s)
        vowel = "aeiouAEIOU"
        i = 0
        j = len(str_list) - 1

        while i <= j:
            if str_list[i] in vowel and str_list[j] in vowel:
                temp = str_list[i]
                str_list[i] = str_list[j]
                str_list[j] = temp
                j -= 1
                i += 1
            elif str_list[i] not in vowel:
                i += 1
            else:
                j -= 1
        return "".join(str_list)

