import unittest

def es_primo(value):
    if value < 2:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True

class TestPrimos(unittest.TestCase):
    def test_1(self):
        self.assertEqual(es_primo(1), False)
    def test_2(self):
        self.assertEqual(es_primo(2), True)
    def test_3(self):
        self.assertEqual(es_primo(3), True)
    def test_4(self):
        self.assertEqual(es_primo(4), False)
    def test_5(self):
        self.assertEqual(es_primo(5), True)
    def test_6(self):
        self.assertEqual(es_primo(6), False)
    def test_7(self):
        self.assertEqual(es_primo(7), True)
unittest.main()