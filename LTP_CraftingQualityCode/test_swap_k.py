import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_empty_list_k0(self):
        """
        Tests function swap_k when L = []
        and k = 0
        """
        
        k = 0
        L = [] 
        L_expected = []
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_single_item_k0(self):
        """
        Tests function swap_k when L = [1]
        and k = 0
        """
        
        k = 0
        L = [1] 
        L_expected = [1]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_evenL_k0(self):
        """
        Tests function swap_k when L = [1, 2]
        and k = 0
        """
        
        k = 0
        L = [1, 2] 
        L_expected = [1, 2]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_evenL_k1(self):
        """
        Tests function swap_k when L = [1, 2]
        and k = 1
        """
        
        k = 1
        L = [1, 2] 
        L_expected = [2, 1]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_evenL_k2(self):
        """
        Tests function swap_k when L = [1, 2, 3, 4, 5, 6]
        and k = 2
        """
        
        k = 2
        L = [1, 2, 3, 4, 5, 6]
        L_expected = [5, 6, 3, 4, 1, 2]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_evenL_k3(self):
        """
        Tests function swap_k when L = [1, 2, 3, 4, 5, 6]
        and k = 3
        """
        
        k = 3
        L = [1, 2, 3, 4, 5, 6]
        L_expected = [4, 5, 6, 1, 2, 3]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_oddL_k1(self):
        """
        Tests function swap_k when L = [1, 2, 3]
        and k = 1
        """
        
        k = 1
        L = [1, 2, 3]
        L_expected = [3, 2, 1]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_oddL_k2(self):
        """
        Tests function swap_k when L = [1, 2, 3, 4, 5]
        and k = 2
        """
        
        k = 2
        L = [1, 2, 3, 4, 5]
        L_expected = [4, 5, 3, 1, 2]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

    def test_oddL_k3(self):
        """
        Tests function swap_k when L = [1, 2, 3, 4, 5, 6, 7]
        and k = 3
        """
        
        k = 3
        L = [1, 2, 3, 4, 5, 6, 7]
        L_expected = [5, 6, 7, 4, 1, 2, 3]
        
        a1.swap_k(L, k)
        
        self.assertEqual(L, L_expected)

if __name__ == '__main__':
    unittest.main(exit=False)
