import unittest

from kwic2 import compareTo
from kwic2 import getLowestNonIndexedWord
import kwic2

class TestKwic2(unittest.TestCase):

    def setUp(self):
        self.kwic2 = kwic2
        self.kwic2.excludedWords = ['the', 'in']
        self.kwic2.lines2BIndexed = [['the','rain','in','spain','falls'],
                                     ['mainly', 'on','the','plain'], ['mainly']]
    def test_compareTo(self):
        self.assertEqual(self.kwic2.compareTo(0,0,0,1),1 ,"'the' comes after 'rain'. ")

    def test_compareTo2(self):
        self.assertEqual(self.kwic2.compareTo(1,0,0,3),-1 ,"'mainly' should come before 'spain'. ")

    def test_compareTo3(self):
        self.assertEqual(self.kwic2.compareTo(0,0,0,0),0 ,"'the' has the same order as itself ")

    def test_compareTo4(self):
        self.assertEqual(self.kwic2.compareTo(0,0,1,2),-1 ,"'the' is before second 'the' ")

    def test_compareTo42(self):
        self.assertEqual(self.kwic2.compareTo(1,2,0,0),1 ,"'the' is before second 'the' ")

    def test_compareTo5(self):
        self.assertEqual(self.kwic2.compareTo(0,4,1,1),-1 ,"'falls' should be before 'on' ")

    def test_compareTo6(self):
        self.assertEqual(self.kwic2.compareTo(1,1,0,4),1 ,"'falls' should be before 'on' ")

    def test_compareTo7(self):
        self.assertEqual(self.kwic2.compareTo(0,4,1,0),-1 ,"'falls' should be before 'mainly' ")


    def test_nextWord1(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(None,None), [0,4], "Falls should be first.")

    def test_nextWord2(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(0,4), [1,0], "'mainly' should be 2nd.")

    def test_nextWord3(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(1,0), [2,0], "'mainly' should be third.")

    def test_nextWord4(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(2,0), [1,1], "'on' should be 4th.")

    def test_nextWord5(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(1,1), [1,3], "'plain' should be 5th.")

    def test_nextWord6(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(1,3), [0,1], "'rain' should be 6th.")

    def test_nextWord7(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(0,1), [0,3], "'spain' should be 7th.")

    def test_nextWord8(self):
        self.assertEqual(self.kwic2.getLowestNonIndexedWord(0,3), [None,None], "'None' should be last.")


    def test_splitLineIntoTriple1(self):
        # Test a middle element of a line
        self.assertEqual(self.kwic2.splitLineIntoTriple(0,3), ['the rain in','spain','falls'], "We should get a triple of this form")

    def test_splitLineIntoTriple2(self):
        # Test the first element of a line
        self.assertEqual(self.kwic2.splitLineIntoTriple(0,0), [ '' ,'the', 'rain in spain falls'], "We should get a triple of this form")

    def test_splitLineIntoTriple3(self):
        # Test the last element of a line
        self.assertEqual(self.kwic2.splitLineIntoTriple(0,4), [ 'the rain in spain', 'falls', ''], "We should get a triple of this form")

    # def test_printFormattedTriple(self):
    #     self.assertEqual(self.kwic2.printFormattedTriple(["happy", "birthday", "mr kennedy"]),
    #                      "         ,         ,         ,         ,         ,         ,         ,")

    def test_printFormattedTriple2(self):
        self.assertEqual(self.kwic2.printFormattedTriple(["happy", "birthday", "mr kennedy"]),
                         "                       happy BIRTHDAY mr kennedy")


if __name__ == "__main__":
    unittest.main()