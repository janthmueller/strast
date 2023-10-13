import unittest
from strast.core import strast


class TestStrastFunction(unittest.TestCase):
    def test_basic_transformation(self):
        self.assertEqual(strast("123"), 123)

    def test_type_checking(self):
        with self.assertRaises(ValueError):
            strast("123", str)


if __name__ == "__main__":
    unittest.main()
