months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
startDay = 1 # 1st January 1901 was a monday
numFirstSundays = 0

for year in range(1901, 2001):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[1] = 29
    else:
        months[1] = 28


    for month in months:
        if startDay == 6:
            numFirstSundays += 1

        startDay = (startDay + month) % 7
print(numFirstSundays)

# Can see what day the start of the month falls on by adding the start day of the previous months to the number of days in that month and modulus 7 from that calculation (as 7 days in a week)