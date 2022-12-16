import unittest
import day2.rps 

class RpsTest(unittest.TestCase):
    def test(self):
        test_guide = (
            "A Y\n"
            "B X\n"
            "C Z\n"
        )
        self.assertEqual(day2.rps.score_guide(test_guide), 15, "score should be 15")
if __name__ == "__main__":
    unittest.main()