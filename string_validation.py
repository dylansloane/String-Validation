#title
print("---STRING VALIDATION---\n")


#procedure to validate the string
def validateString(string):


    
    #1: check if first character is a capital letter
    if string[0].isupper():
        print("Rule 1 passed...")
    else:
        print("Rule 1 failed! The string must start with a capital letter. Please try again.\n")
        menu()


    
    #2: check if string has an even number of quotation marks
    quotationCounter = 0

    #iteration
    for character in string:

        #count the number of quotation marks
        if character == '"':
            quotationCounter += 1

    #check if the value is even (check if remainder is 0 when divided by 2)
    if quotationCounter % 2 == 0:
        print("Rule 2 passed...")
    else:
        print("Rule 2 failed! The string must have an even number of quotation marks. Please try again.\n")
        menu()


    
    #3: check if the string ends in either '.' , '?' or '!'
    if string[-1] in ['.', '!', '?']:
        print("Rule 3 passed...")
    else:
        print("Rule 3 failed! The string must end in either '.' , '?' or '!'. Please try again.\n")
        menu()
    

    
    #4: check if the string has no other period characters other than the last character
    periodCounter = 0

    #iteration
    for character in string:

        #count the number of periods
        if character == '.':
            periodCounter += 1
        
    #create valid bool and check if valid
    periodValid = False

    #cannot be more than one
    if periodCounter > 1:
        periodValid = False

    #make sure that if there is only one, it must be the end character
    elif periodCounter == 1 and string[-1] == '.':
        periodValid = True

    #could be 0 if the string ends in '!' or '?'
    elif periodCounter == 0:
        periodValid = True

    #evaluate validity
    if periodValid == True:
        print("Rule 4 passed...")
    else:
        print("Rule 4 failed! The string must have no period characters, unless it is the last one. Please try again.\n")
        menu()


    
    #5. check if numbers in the string below 13 are spelled out
    currentNumber = ""

    #iteration
    for character in string:

        #check if character is a digit
        if character.isdigit():

            #append currentNumber variable
            currentNumber += character
        
        else:

            #check the final current number is not empty
            if currentNumber != "":

                #check if the number is less than 13
                if int(currentNumber) < 13:

                    #invalid
                    print("Rule 5 failed! Any number below 13 must be spelled out. Please try again.\n")
                    menu()
                
                #valid
                else:
                    print("Rule 5 passed...\nOutcome: The input string is valid.\n")
                    return True
                menu()
                

                 




#create a menu, so that the code will not finish unless the user quits
def menu():

    #menu layout
    menuInput = input("1. Enter String\n2. Quit\nEnter Choice: ")

    #user enters string
    if menuInput == "1":
        stringInput = str(input("\nEnter a string: "))
        validateString(stringInput)

    #user quits
    elif menuInput == "2":
        quit()

    #user enters invalid input
    else:
        print("Enter either 1 or 2. Please try again.\n")
        menu()





#run
menu()