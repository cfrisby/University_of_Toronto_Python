import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_n_0(self):
        """
        Tests function num_buses when n = 0.
        """

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_n_1(self):
        """
        Tests function num_buses when n = 1.
        """

        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_n_49(self):
        """
        Tests function num_buses when n = 49.
        """

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(expected, actual)

    def test_n_50(self):
        """
        Tests function num_buses when n = 50.
        """

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_n_51(self):
        """
        Tests function num_buses when n = 51.
        """

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)

    def test_n_100(self):
        """
        Tests function num_buses when n = 100.
        """

        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(expected, actual)

    def test_n_75(self):
        """
        Tests function num_buses when n = 75.
        """

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(expected, actual)

    def test_n_365(self):
        """
        Tests function num_buses when n = 365.
        """

        actual = a1.num_buses(365)
        expected = 8
        self.assertEqual(expected, actual)

    

if __name__ == '__main__':
    unittest.main(exit=False)
