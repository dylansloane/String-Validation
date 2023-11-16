import unittest

#functions to validate the string

def rule1(string):
    if string[0].isupper():
        return True
    else:
        return False

def rule2(string):
    quotationCounter = 0
    for character in string:
        if character == '"':
            quotationCounter += 1
    if quotationCounter % 2 == 0:
        return True
    else:
        return False

def rule3(string):
    if string[-1] in [".", "!", "?"]:
        return True
    else:
        return False

def rule4(string):
    periodCounter = 0
    for character in string:
        if character == ".":
            periodCounter += 1
    if periodCounter == 1 and string[-1] == ".":
        return True
    elif periodCounter == 0:
        return True
    else:
        return False

def rule5(string):
    currentNumber = ""
    for character in string:
        if character.isdigit():
            currentNumber += character
        else:
            if currentNumber != "":
                if int(currentNumber) < 13:
                    return False
                else:
                    return True
    if currentNumber == "":
        return True

class TestValidateString(unittest.TestCase):

    #captial letter as first character
    def test_rule1(self):
        self.assertEqual(rule1("The quick brown fox said “hello Mr lazy dog”."), True)
        self.assertEqual(rule1("the quick brown fox said “hello Mr lazy dog”."), False)

    #even number of quotation marks
    def test_rule2(self):
        self.assertEqual(rule2('The quick brown fox said hello Mr lazy dog.'), True)
        self.assertEqual(rule2('The quick brown fox said hello Mr lazy dog."'), False)

    #string ends with termination character
    def test_rule3(self):
        self.assertEqual(rule3("The quick brown fox said hello Mr lazy dog."), True)
        self.assertEqual(rule3("The quick brown fox said hello Mr lazy dog"), False)

    #string has no period characters other than the last
    def test_rule4(self):
        self.assertEqual(rule4("The quick brown fox said hello Mr lazy dog."), True)
        self.assertEqual(rule4("The quick brown fox said hello Mr. lazy dog"), False)

    #numbers below 13 are spelled out
    def test_rule5(self):
        self.assertEqual(rule5("The quick brown fox said hello Mr lazy dog one time."), True)
        self.assertEqual(rule5("The quick brown fox said hello Mr. lazy dog 1 time"), False)


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass