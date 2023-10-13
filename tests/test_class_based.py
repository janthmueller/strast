import unittest
from strast.class_based import Strast


class TestStrastClass(unittest.TestCase):
    def test_transform_method(self):
        strast_obj = Strast(int)
        self.assertEqual(strast_obj.transform("123"), 123)

    def test_call_method(self):
        strast_obj = Strast(int)
        self.assertEqual(strast_obj("123"), 123)


if __name__ == "__main__":
    unittest.main()
