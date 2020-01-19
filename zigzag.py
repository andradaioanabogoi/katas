class ZigZag:

    def convert(self, input_string, numRows):
        result = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
        for i, j in enumerate(input_string):
            result[i % (numRows+2)] += j
        print(result)
        for k in [0, (numRows+2)/2]:
            print(result[k] + result[numRows + 2 - k])


print(ZigZag().convert("PAYPALISHIRING", 4))
