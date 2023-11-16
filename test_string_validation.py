import unittest
from string_rules import rule1, rule2, rule3, rule4, rule5

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