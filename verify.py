#!/usr/bin/env python3

"""
Test script for Look And Say code.
"""



EXPECTED_OUTPUT = b"""11223344
21222324
121132131214
1112211312111311121114
312221131112311331123114
"""

import unittest, subprocess

class TestLookAndSay(unittest.TestCase):
    def test_lookandsay_order5_defaultRuntype(self):
        outstr = subprocess.check_output("python3 lookandsay.py 1223334444 5".split())
        self.assertEqual(EXPECTED_OUTPUT, outstr)

    def test_lookandsay_order5_naiveRuntype(self):
        outstr = subprocess.check_output("python3 lookandsay.py --naive 1223334444 5".split())
        self.assertEqual(EXPECTED_OUTPUT, outstr)

    def test_lookandsay_order5_bufgenRuntype(self):
        outstr = subprocess.check_output("python3 lookandsay.py --bufgen 1223334444 5".split())
        self.assertEqual(EXPECTED_OUTPUT, outstr)

    # def test_lookandsay_order5_bufferRuntype(self):
    #     outstr = subprocess.check_output("python3 lookandsay.py --buffer 1223334444 5".split())
    #     self.assertEqual(EXPECTED_OUTPUT, outstr)

if __name__ == '__main__':
    unittest.main()
