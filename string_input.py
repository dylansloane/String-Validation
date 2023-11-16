import string_rules

#create a menu, so that the code will not finish unless the user quits
def menu():

    #menu layout
    menuInput = input("1. Enter String\n2. Quit\nEnter Choice: ")

    #user enters string
    if menuInput == "1":
        stringInput = str(input("\nEnter a string: "))

        #validate rule 1
        if not string_rules.rule1(stringInput):
            print("Rule 1 failed! The string must start with a capital letter. Please try again.\n"), menu()
        print("Rule 1 passed...")

        #validate rule 2
        if not string_rules.rule2(stringInput):
            print("Rule 2 failed! The string must have an even number of quotation marks. Please try again.\n"), menu()
        print("Rule 2 passed...")

        #validate rule 3
        if not string_rules.rule3(stringInput):
            print("Rule 3 failed! The string must end in either '.' , '?' or '!'. Please try again.\n"), menu()
        print("Rule 3 passed...")

        #validate rule 4
        if not string_rules.rule4(stringInput):
            print("Rule 4 failed! The string must have no period characters, unless it is the last one. Please try again.\n"), menu()
        print("Rule 4 passed...")

        #validate rule 5
        if not string_rules.rule5(stringInput):
            print("Rule 5 failed! Any number below 13 must be spelled out. Please try again.\n"), menu()
        print("Rule 5 passed...\nOutcome: Valid String.\n"), menu()



    #user quits
    elif menuInput == "2":
        quit()

    #user enters invalid input
    else:
        print("Enter either 1 or 2. Please try again.\n")
        menu()


#run
while True:
    menu()