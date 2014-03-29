#!/usr/bin/env python3
#
# EvalExprTest.py
# Tests for the EvalExpr.py module.

import unittest
from EvalExpr import EvalExpr

class EvalExprTest(unittest.TestCase):
  def testExpressions(self):
    varMap = {"pi": 3.14}
    e = EvalExpr(varMap)
    self.assertAlmostEqual(e.evalExpr("-pi+1"), -2.14)
    self.assertAlmostEqual(e.evalExpr("(20+10)*3/2-3"), 42.0)
    self.assertAlmostEqual(e.evalExpr("1 << 4"), 16.0)
    self.assertAlmostEqual(e.evalExpr("1+(-2*3)"), -5.0)

if __name__ == '__main__':
    unittest.main()
