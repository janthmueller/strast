import unittest
import strast


class TestStrastFunction(unittest.TestCase):
    def test_basic_transformation(self):
        self.assertEqual(strast.c("123"), 123)
        self.assertEqual(strast.c("1.23"), 1.23)
        self.assertEqual(strast.c("{1: 2, 3: 4}"), {1: 2, 3: 4})
        self.assertEqual(strast.c("[1, 2, 3]"), [1, 2, 3])
        self.assertEqual(strast.c("'123'"), "123")
        self.assertEqual(strast.c("{1,2,3}"), {1, 2, 3})
        self.assertEqual(strast.c("None"), None)
        self.assertEqual(strast.c(123), 123)

    def test_type_checking(self):
        self.assertEqual(strast.c("123", int), 123)
        self.assertEqual(strast.c("1.23", float), 1.23)
        self.assertEqual(strast.c("{1: 2, 3: 4}", dict), {1: 2, 3: 4})
        self.assertEqual(strast.c("[1, 2, 3]", list), [1, 2, 3])
        self.assertEqual(strast.c("'123'", str), "123")
        self.assertEqual(strast.c("{1,2,3}", set), {1, 2, 3})
        self.assertEqual(strast.c("None", None, grab_types=None), None)
        self.assertEqual(strast.c(123, int), 123)
        self.assertEqual(strast.c(None, float, None), None)

    def test_raises(self):
        with self.assertRaises(ValueError):
            strast.c("123", str)
        with self.assertRaises(ValueError):
            strast.c(123, str)
        with self.assertRaises(TypeError):
            strast.c(
                "hello world", "this should be interpreted as a string", grab_types=None
            )
        with self.assertRaises(TypeError):
            strast.c(123, force_str=True)
        with self.assertRaises(ValueError):
            strast.c("hello", str, force_ast=True)  # should be "'hello'"


if __name__ == "__main__":
    unittest.main()
