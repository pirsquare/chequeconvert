import unittest
from chequeconvert.base import generate_word


class TestBase(unittest.TestCase):

    def test_generate_word(self):
        ret = generate_word("30")
        self.assertEquals(ret, "Thirty Only")

        ret = generate_word("0.01")
        self.assertEquals(ret, "Cents One Only")

        ret = generate_word("0.5")
        self.assertEquals(ret, "Cents Fifty Only")

        ret = generate_word("120")
        self.assertEquals(ret, "One Hundred And Twenty Only")

        ret = generate_word("12,220.4")
        self.assertEquals(ret, "Twelve Thousand Two Hundred And Twenty And Cents Forty Only")

        ret = generate_word("501,932.03")
        self.assertEquals(ret, "Five Hundred And One Thousand Nine Hundred And Thirty Two And Cents Three Only")

        ret = generate_word("211, 455, 002.13")
        self.assertEquals(
            ret, "Two Hundred And Eleven Million Four Hundred And Fifty Five Thousand Two And Cents Thirteen Only")

        ret = generate_word("99, 011, 030, 052.22")
        self.assertEquals(
            ret, "Ninety Nine Billion Eleven Million Thirty Thousand Fifty Two And Cents Twenty Two Only")

        ret = generate_word("100, 000, 000, 000")
        self.assertEquals(ret, "One Hundred Billion Only")

        # assert exception when more than 100 billion is provided
        self.assertRaises(Exception, generate_word, "100, 000, 000, 000.01")

        # assert exception when more than 2 decimal place is provided
        self.assertRaises(Exception, generate_word, "0.015")
