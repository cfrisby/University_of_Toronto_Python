import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_empty_list(self):
        """
        Tests function stock_price_summary when
        price_changes = []
        """

        actual = a1.stock_price_summary([])
        expected = (0.00, 0.00)
        self.assertEqual(expected, actual)

    def test_single_zero(self):
        """
        Tests function stock_price_summary when
        price_changes = [0.00]
        """

        actual = a1.stock_price_summary([0.00])
        expected = (0.00, 0.00)
        self.assertEqual(expected, actual)

    def test_single_positive(self):
        """
        Tests function stock_price_summary when
        price_changes = [0.1]
        """

        actual = a1.stock_price_summary([0.1])
        expected = (0.10, 0.00)
        self.assertEqual(expected, actual)

    def test_single_negative(self):
        """
        Tests function stock_price_summary when
        price_changes = [-0.1]
        """

        actual = a1.stock_price_summary([-0.1])
        expected = (0.00, -0.10)
        self.assertEqual(expected, actual)

    def test_all_positive(self):
        """
        Tests function stock_price_summary when
        price_changes = [0.1, 0.02, 0.08, 0.12, 0.01]
        """

        actual = a1.stock_price_summary([0.1, 0.02, 0.08, 0.12, 0.01])
        expected = (0.33, 0.00)
        self.assertEqual(expected, actual)

    def test_all_negative(self):
        """
        Tests function stock_price_summary when
        price_changes = [-0.1, -0.02, -0.08, -0.12, -0.01]
        """

        actual = a1.stock_price_summary([-0.1, -0.02, -0.08, -0.12, -0.01])
        expected = (0.00, -0.33)
        self.assertEqual(expected, actual)

    def test_all_zero(self):
        """
        Tests function stock_price_summary when
        price_changes = [0, 0, 0, 0, 0, 0, 0, 0]
        """

        actual = a1.stock_price_summary([0, 0, 0, 0, 0, 0, 0, 0])
        expected = (0.00, 0.00)
        self.assertEqual(expected, actual)

    def test_general_case(self):
        """
        Tests function stock_price_summary when
        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]
        """

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
