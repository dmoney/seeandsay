#!/usr/bin/env python3

"""
Test script for Look And Say code.
"""



EXPECTED_OUTPUT = b"""11223344
21222324
121132131234
1112211312111311121314
3122211311123113311211131114
"""

import unittest, subprocess

class TestLookAndSay(unittest.TestCase):
    def test_lookandsay_order5(self):
        outstr = subprocess.check_output("python3 lookandsay.py 1223334444 5".split())
        self.assertEqual(EXPECTED_OUTPUT, outstr)

if __name__ == '__main__':
    unittest.main()
