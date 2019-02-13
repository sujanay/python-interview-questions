import sys
from math import pi

class constantDiary:
    diaryContent = {}
    diaryDates = []
    _diaryNumber = 1

    def writeInDiary(self, date, entry):
        self.diaryDates.append(date)
        self.diaryContent[date] = entry

    def readDiary(self):
        for i in range(1,3):
            print(self.diaryContent[i]),
        
        print(self._diaryNumber)

def main():
    myDiary = constantDiary()
    myDiary.writeInDiary(1, "I like apple sauce")
    myDiary.writeInDiary(2, "I don't like it anymore")

    myDiary.readDiary()

    return 0

main()               # Output
                     # I like apple sauce
                     # I don't like it anymore
                     # 1