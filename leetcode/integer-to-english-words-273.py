class Solution(object):
    def __init__(self):
        self.appendix = ['', 'Thousand', 'Million', 'Billion']
        self.nums = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    def numberToWordsHelper(self, num):
        """
        :type num: int
        :rtype: str
        """
        numStr = str(num)
        
        if (len(numStr) == 1):
            return self.nums[num]
        elif (len(numStr) == 2):
            if (num / 10 == 1):
                return self.teens[num % 10]
            else:
                return self.tens[num / 10 - 2] + ('' if num % 10 == 0 else ' ' + self.nums[num % 10])
        elif (len(numStr) == 3):
            again = self.numberToWordsHelper(num % 100)
            return self.nums[num / 100] + ' Hundred' + ('' if again == '' else ' ' + again)


    def numberToWords(self, num):
        if (num == 0):
            return 'Zero'

        numStr = str(num)
        secs = (len(numStr) - 1) / 3
        
        temp = num
        cnt = 0
        returnStr = ''
        while temp != 0:
            again = self.numberToWordsHelper(temp % 1000)
            returnStr = ('' if again == '' else again + ' ' + self.appendix[cnt] + ' ') + returnStr
            cnt += 1
            temp = temp / 1000

        return returnStr.strip()
        
# Cases that we missed originally: 
#   One billion
#   123 having trailing spaces because of appendix[0] = ''
if __name__ == '__main__':
    sol = Solution()
    print(sol.numberToWords(1111111111))
