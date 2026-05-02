import math

def calculate():
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
    thousands = ["", "onethousand"]

    numbers = ""
    for i in range(1, 1000):
        unitsFrom = i

        while unitsFrom != 0:
            logVal = 10**int(math.log10(unitsFrom))
            digit = unitsFrom // logVal
            if len(str(unitsFrom)) == 3:
                if str(unitsFrom)[1:] == "00":
                    numbers += hundreds[digit]
                else:
                    numbers += (hundreds[digit] + "and")

            elif len(str(unitsFrom)) == 2:
                if digit != 1:
                    numbers += tens[digit]
                else:
                    digit = int(str(unitsFrom)[-1])
                    numbers += teens[digit]
                    break

            else:
                numbers += ones[digit]

            unitsFrom = unitsFrom % logVal

    return len(numbers) + len(thousands[-1])

print(calculate())

 