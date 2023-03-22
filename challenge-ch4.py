# Create a program that counts the number of a specific weekday during a given month and year.
# Ex: Count the number of Sundays in January in 2024
# User can type "exit" to quit the program
# Hint: use monthcalendar class

import calendar

# myBirthMonth = calendar.monthcalendar(1974, 9)
# print(myBirthMonth)
# print(len(myBirthMonth))
# print(myBirthMonth[0][6])

runTheCheck = True
while(runTheCheck):
    theWeekdays = {
        "0": "Monday",
        "1": "Tuesday",
        "2": "Wednesday",
        "3": "Thursday",
        "4": "Friday",
        "5": "Saturday",
        "6": "Sunday"
    }

    theMonths = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    # get the day from the user
    print("0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday.")
    testDay = input("Enter the number for the day you want to count: ")
    # convert the string to lowercase
    testDay = testDay.lower()
    # print(type(testDay))
    # if the user enters 'exit', quit the program
    if testDay.lower() == "exit":
        runTheCheck = False
        print("See ya")
        break
    else:
        if (int(testDay) < 0) or (int(testDay) > 6):
            testDay = input("You did not enter a valid day. Enter a valid day to count:")
        else:
            print("You want to check for", theWeekdays[testDay])
            break
            # print("1=January, 2=February, 3=March, 4=April, 5=May, 6=June, 7=July, 8=August, 9=September, 10=October, 11=November, 12=December.")
            # testMonth = input("Enter the number for the month: ")
            # # get the  month
            # # print(type(testMonth))
            # if (int(testMonth) < 1) or (int(testMonth) > 12):
            #     testMonth = input("You did not enter a valid month. Enter a valid month:")
            # else:
            #     print("You want to check for", theMonths[testMonth])