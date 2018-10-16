# returns true if it's a leap year
def isLeapYear(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0): #is divisible by 4, unless it's divisible by 100, except when it's divisible by 400
        return True
    return False

# gives the length of a month, given a month and if it's a leap year
def monthlength(month, boolLeap):
    monthlength = 0
    if month == 2:
        if boolLeap:
            monthlength = 29
        else:
            monthlength = 28
    elif month in [4,6,9,11]:
        monthlength = 30
    else:
        monthlength = 31
    return monthlength

# guesses tomorrow's date
def tommorowsdate(year, month, day):
    Leap = isLeapYear(year)
    length = monthlength(month, Leap)
    if day < length:
        day += 1
    elif month == 12:
        day = 1
        month = 1
        year += 1
    else:
        day = 1
        month += 1
    return str(year) + "/" + str(month) + "/" +str(day)

while True:
    year = int(input("Enter a year: "))
    month = int(input("Please enter the current numerical month (MM): ")) 
    day = int(input("Please enter the current numerical day (DD): "))
    while day > monthlength(month,isLeapYear(year)):
        day = int(input("Please enter a valid day: "))
    print("\nThe current date is:", str(year) + "/" + str(month) + "/" +str(day) + ".")
    print("Tomorrow's date is: ", end="")
    print(tommorowsdate(year, month, day),"\n")    