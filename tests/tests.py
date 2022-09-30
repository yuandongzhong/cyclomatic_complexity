import unittest
import os
from cyclo.calculate import calculate

class TestCalcMetric(unittest.TestCase):
    def test_birds(self):
        with open(os.path.dirname(__file__) + "test/src/birds.py", "r") as file:
            source = file.read()
            analyzer = calculate(source)
            self.assertEqual(analyzer.total, 10)


if __name__ == '__main__':
    unittest.main()