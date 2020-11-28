import unittest
import pandas as pd
import numpy as np

class TestPreprocessing(unittest.TestCase):
    X = pd.DataFrame(np.random.randint(0, 100, size=(4, 4)), columns=list('ABCD'))
    X.head()
    #def test_dealWithMissingValues():
