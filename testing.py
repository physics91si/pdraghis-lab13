#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    
    def testAddition(self):
        self.assertEqual(calc.calc('1+1'), 2)

    def testSubtraction(self):
        self.assertEqual(calc.calc('11-10'), 1)

    def testMultiplciation(self):
        self.assertEqual(calc.calc('10*12'), 120)
 
    def testDivision(self):
        self.assertEqual(calc.calc('10/2'), 5)

if __name__ == '__main__':
    unittest.main()

