class TelephoneNumber:
    def __init__(self, NUMBER_LENGTH, phoneNum):
        self.NUMBER_LENGTH = NUMBER_LENGTH
        self.phoneNum = phoneNum

    def telephoneNumber(self, n):
        self.phoneNum = n

    def printWords(self, currentDigit):
        if(currentDigit == self.NUMBER_LENGTH):
            print(char(self.NUMBER_LENGTH))
            return 0
        for(i in range(1, 3)):
            result[currentDigit] = getCharKey(phoneNum[currentDigit], i)
            printWords(self, currentDigit+1)
            if(phoneNum(self, currentDigit) == 0 | phoneNum(self, currentDigit) == 1):
                return 0
