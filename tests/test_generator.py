import unittest
from generator import Generator


class GeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.random_testimony = "Wir mUssen wissen, wir werden wissen!"


class TestGenerator(GeneratorTestCase):
    def test_add_testimony(self):
        self.generator.add_testimony(self.random_testimony)

        self.assertTrue(self.generator.has_testimony(self.random_testimony))

    def test_has_testimony(self):
        self.generator.testimonies.append(self.random_testimony)

        self.assertTrue(self.generator.has_testimony(self.random_testimony))

    def test_generate_testimony(self):
        self.generator.add_testimony(self.random_testimony)
        result_testimony = self.generator.generate_testimony()
        self.assertTrue(self.generator.has_testimony(result_testimony))

    def test_remove_testimony(self):
        self.generator.add_testimony(self.random_testimony)
        self.generator.remove_testimony(self.random_testimony)
        self.assertFalse(self.generator.has_testimony(self.random_testimony))


if __name__ == '__main__':
    unittest.main()
