import unittest
import strast


class TestStrastFactory(unittest.TestCase):
    def test_factory_creation(self):
        my_strast = strast.f(int)
        self.assertEqual(my_strast("123"), 123)


if __name__ == "__main__":
    unittest.main()
