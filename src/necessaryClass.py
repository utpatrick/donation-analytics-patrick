class Donor:
    def __init__(self, CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT):
        self.CMTE_ID = CMTE_ID
        self.NAME = NAME
        self.ZIP_CODE = ZIP_CODE
        self.TRANSACTION_DT = TRANSACTION_DT
        self.TRANSACTION_AMT = TRANSACTION_AMT

    def __str__(self):
        return "CMTE_ID=" + self.CMTE_ID + \
                "|NAME=" + self.NAME + \
                "|ZIP_CODE=" + self.ZIP_CODE + \
                "|TRANSACTION_DT=" + str(self.TRANSACTION_DT) + \
                "|TRANSACTION_AMT=" + self.TRANSACTION_AMT


class Campaign:
    def __init__(self, YEAR, TOTAL_AMOUNT=[], SUM=0, LEN=0):
        self.YEAR = YEAR
        self.TOTAL_AMOUNT = TOTAL_AMOUNT
        self.SUM = SUM
        self.LEN = LEN

    def __str__(self):
        return "YEAR=" + self.YEAR + \
                "SUM=" + self.SUM + \
                "LEN=" + self.LEN

    def updateSum(self, newAmount):
        self.LEN += 1
        self.TOTAL_AMOUNT.append(newAmount)
        self.SUM += newAmount