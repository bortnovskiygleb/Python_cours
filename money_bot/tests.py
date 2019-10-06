import unittest
from main import money, answer


class BotTest(unittest.TestCase):
    def test_money(self):
        self.assertEqual(money, "BYN")

    def test_answer(self):
        self.assertIsInstance(answer, dict)


if __name__ == '__main__':
    unittest.main()
