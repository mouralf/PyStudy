#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
import unittest

def oddNumbers(l, r):
    # Write your code here
    odds = []
    
    for n in range(l, r+1, 1):
        if (n%2 != 0):
            odds.append(n)
        else:
            pass
    
    return odds
    
class TestOddNumbers(unittest.TestCase):
    def test_oddN(self):
        self.assertEqual(oddNumbers(2,5),[3,5])
        self.assertEqual(oddNumbers(3,9),[3,5,7,9])
        
    
    
    
    
if __name__ == '__main__':
  
    unittest.main()