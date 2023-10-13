import unittest
from strast import strastf


class TestStrastFactory(unittest.TestCase):
    def test_factory_creation(self):
        my_strast = strastf(int)
        self.assertEqual(my_strast("123"), 123)


if __name__ == "__main__":
    unittest.main()
