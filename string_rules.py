#create different procedures to validate the string
def rule1(string):

    #1: check if first character is a capital letter
    if string[0].isupper():
        return True
    else:
        return False


def rule2(string):
    #2: check if string has an even number of quotation marks
    quotationCounter = 0

    #iteration
    for character in string:

        #count the number of quotation marks
        if character == '"':
            quotationCounter += 1

    #check if the value is even (check if remainder is 0 when divided by 2)
    if quotationCounter % 2 == 0:
        return True
    else:
        return False


def rule3(string):
    #3: check if the string ends in either '.' , '?' or '!'
    if string[-1] in ['.', '!', '?']:
        return True
    else:
        return False
    

def rule4(string):
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
        return True
    else:
        return False


def rule5(string):
    #5. check if numbers in the string below 13 are spelled out
    currentNumber = ""
    numbers = []

    #iteration
    for character in string:

        #check if character is a digit
        if character.isdigit():

            #append currentNumber variable
            currentNumber += character
        
        #if the character is not a digit
        else:

            #add number to array
            try:
                numbers.append(int(currentNumber))
            except ValueError:
                pass

            #reassign current number as empty
            currentNumber = ""
                
    #valid boolean
    valid = True

    #return true if there are no numbers in the string
    if len(numbers) == 0:
        return True
    
    #check the array for any numbers below 13
    else:
        for i in range(13):
            if i in numbers:
                valid = False
        return valid
