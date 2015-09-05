class Solution(object):
    # Karatsuba multiplication implementation 
    minimumNumOfDigits = 10

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if (len(num1.lstrip("0")) == 0 or len(num2.lstrip("0")) == 0):
            return "0"
        return self.karatsuba(num1.lstrip("0"), num2.lstrip("0")).lstrip("0")

    def stringMinus(self, num1, num2):
    	"""
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if (len(num2) > len(num1)):
        	#print('Error: minus results in negative')
            pass

        idx = -1
        carry = 0

        str1 = num1[::-1]
        str2 = num2.zfill(len(num1))
        res = ""

        for c1 in str1:
            temp = int(c1) - int(str2[idx]) - carry
            if temp < 0:
            	carry = 1
            	temp = temp + 10
            else:
            	carry = 0
            idx -= 1
            res += str(temp)

        if carry != 0:
        	#print('Error: minus results in negative')
            pass
        
        return res[::-1].lstrip("0")

    def stringPlus(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        idx = -1
        carry = 0
        digits = max(len(num1), len(num2))

        str1 = num1.zfill(digits)[::-1]
        str2 = num2.zfill(digits)
        res = ""

        for c1 in str1:
            temp = int(c1) + int(str2[idx]) + carry
            if temp > 9:
            	carry = 1
            	temp = temp - 10
            else:
            	carry = 0
            idx -= 1
            res += str(temp)

        res = res + str(carry)

    	return res[::-1].lstrip("0")

    def shortStringMultiply(self, num1, num2):
        '''
        if (len(num1.lstrip("0")) == 0 or len(num2.lstrip("0")) == 0):
            return "0"
        res = ""
        if (len(num1) < self.minimumNumOfDigits):
            for i in range(0, int(num1)):
                res = self.stringPlus(res, num2)
        else:
            for i in range(0, int(num2)):
                res = self.stringPlus(res, num1)
        return res.lstrip("0")
        '''
        if num1 == "" or num2 == "":
            return "0"
        return str(int(num1) * int(num2))

    # 0 edge case; large diff in len case
    def karatsuba(self, num1, num2):
    	"""
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if (len(num1) < self.minimumNumOfDigits or len(num2) < self.minimumNumOfDigits):
        	return self.shortStringMultiply(num1, num2)
            #res = self.shortStringMultiply(num1, num2)
        	#return res

        maxLen = max(len(num1), len(num2))
        num1 = num1.zfill(maxLen)
        num2 = num2.zfill(maxLen)
        threshold = maxLen / 2
        high1 = num1[:threshold]
        low1 = num1[threshold:]
        fill = maxLen - threshold

        high2 = num2[:threshold]
        low2 = num2[threshold:]

        z0 = self.karatsuba(high1, high2)
        z1 = self.karatsuba(self.stringPlus(high1, low1), self.stringPlus(high2, low2))
        z2 = self.karatsuba(low1, low2)

        return self.stringPlus(self.stringPlus(z0 + "0" * fill * 2, self.stringMinus(self.stringMinus(z1, z0), z2) + "0" * fill), z2)

if __name__ == "__main__":
	sol = Solution()
	#print(sol.stringPlus('42019481094', '4302942384903240238'))
	#print(sol.multiply('327627058702778602539273796517171833851621821801164203772344061466', '43826220310628268637074692938715119932983147093078095467672675187190581895716023823681540707347276446528399'))
