runTheCheck = True
while(runTheCheck):
    # get a string from the user
    testString = input("Enter a string to test for palindrome, or type 'exit': ")
    # convert the string to lowercase
    testString = testString.lower()
    # if the user enters 'exit', quit the program
    if testString == "exit":
        runTheCheck = False
        print("Goodbye")
        break
    else:
        forwardString = ""
        # remove all punctuation and spaces
        for x in testString:
            if x.isalnum():
                forwardString += x
    # compare the original string to its reverse
    if forwardString == forwardString[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")