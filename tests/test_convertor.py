import unittest
from convertor import Convertor


class ConvertorTestCase(unittest.TestCase):

    def setUp(self):
        self.convertor = Convertor("test_data.txt")
        self.file_name = "test_data.txt"
        self.rand_testimony = "asdf\n"


class TestConvertor(ConvertorTestCase):

    def test_add_testimony(self):
        self.convertor.add_testimony("asdf")

        with open("test_data.txt", "r") as f:
            testimonies = f.readlines()
            self.assertTrue("asdf\n" in testimonies)

    def test_add_saved_testimonies(self):
        with open("test_data.txt", "w") as f:
            f.write("asdf\n")

        self.convertor.add_saved_testimonies()
        self.assertTrue(self.convertor.has_testimony(self.rand_testimony))

    def test_remove_testimony(self):
        self.convertor.add_testimony(self.rand_testimony)
        self.convertor.remove_testimony(self.rand_testimony)

        with open("test_data.txt", "r") as f:
            self.assertFalse(self.convertor.has_testimony(self.rand_testimony))


if __name__ == '__main__':
    unittest.main()
