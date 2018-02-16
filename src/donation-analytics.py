import sys
import fileinput
from necessaryClass import *
from helperFunctions import *
from datetime import *
import math

input_dir = sys.argv[1]
perc_dir = sys.argv[2]
output_dir = sys.argv[3]

# input_dir = "../input/itcont.txt"
# perc_dir = "../input/percentile.txt"
# output_dir = "../output/repeat_donors.txt"

percentile = 0
for line in fileinput.input(perc_dir):
    percentile = int(line)

# count = 0
# count_stop = 1000000000

nonRepeatDonor = {} # key = NAME + ZIP_CODE
repeatDonor = {} # key = NAME + ZIP_CODE
campaignRecord = {} # key = CMTE_ID + YEAR

for line in fileinput.input(input_dir):
    # if count > count_stop:
    #     break
    # count += 1

    info = line.split("|")
    CMTE_ID = info[0]
    if CMTE_ID == "":
        continue

    NAME = info[7]
    if not isValidName(NAME):
        continue

    ZIP_CODE = info[10]
    if not isValidZipCode(ZIP_CODE):
        continue
    else:
        ZIP_CODE = ZIP_CODE[:5]

    DONORKEY = NAME + ZIP_CODE

    TRANSACTION_DT = info[13]
    if not isValidTransDate(TRANSACTION_DT):
        continue
    else:
        year = int(TRANSACTION_DT[4:])
        month = int(TRANSACTION_DT[:2])
        day = int(TRANSACTION_DT[2:4])
        TRANSACTION_DT = date(year, month, day)

    TRANSACTION_AMT = info[14]
    if not isValidTransAmount(TRANSACTION_AMT):
        continue

    OTHER_ID = info[15]
    if OTHER_ID != "":
        continue

    thisDonor = Donor(CMTE_ID = CMTE_ID, NAME = NAME, ZIP_CODE = ZIP_CODE,
                      TRANSACTION_DT = TRANSACTION_DT, TRANSACTION_AMT = TRANSACTION_AMT)

    if DONORKEY in nonRepeatDonor.keys():
        donationList = nonRepeatDonor[DONORKEY]
        for record in donationList:
            thisCMTE_ID = thisDonor.CMTE_ID
            recCMTE_ID = record.CMTE_ID
            thisDate = thisDonor.TRANSACTION_DT
            recDate = record.TRANSACTION_DT

            if(thisDate > recDate):
                thisCampaignYear = thisDate.strftime("%Y")
                CMTEKEY = thisCMTE_ID + thisCampaignYear
                if CMTEKEY not in campaignRecord.keys():
                    thisCampaign = Campaign(thisCampaignYear)
                    campaignRecord[CMTEKEY] = thisCampaign
                campaignRecord[CMTEKEY].updateSum(int(thisDonor.TRANSACTION_AMT))
                percentileIndex = math.ceil(percentile/100. * campaignRecord[CMTEKEY].LEN) - 1
                temp = campaignRecord[CMTEKEY].TOTAL_AMOUNT
                temp.sort()
                with open(output_dir, "a") as myfile:
                    myfile.write(thisDonor.CMTE_ID + "|" + \
                                 thisDonor.ZIP_CODE + "|" + \
                                 thisCampaignYear + "|" + \
                                 str(temp[percentileIndex]) + "|"+ \
                                 str(campaignRecord[CMTEKEY].SUM) + "|" + \
                                 str(campaignRecord[CMTEKEY].LEN))
                    myfile.write("\n")
                break
    else:
        nonRepeatDonor[DONORKEY] = []
    nonRepeatDonor[DONORKEY].append(thisDonor)


if __name__ == '__main__':
    print("main")
    #print(output_dir)