import sys

import calculator

import unittest
class calculator_test(unittest.TestCase):

    def setUp(self):
        self.a=20
        self.b=10

    def tearDown(self):
        self.a=0
        self.b=0

    def test_add(self):
        c=calculator.add(self.a,self.b)
        self.assertEqual(self.a+self.b,c)

    def test_sub(self):
        c=calculator.sub(self.a,self.b)
        self.assertEqual(self.a-self.b,c)

    def test_mul(self):
        c=calculator.Mul(self.a,self.b)
        self.assertEqual(self.a*self.b,c)

    @unittest.skipIf(sys.platform.startswith("win"), "requires NOT Windows os")
    def test_div(self):
        c=calculator.div(self.a,self.b)
        self.assertEqual(self.a/self.b,c)

if __name__=="__main__":
    unittest.main()