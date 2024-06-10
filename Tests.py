import unittest
from Adjacency import mat_to_list
from ReachableNodes import reachable

"""Unit-testing for Adjacency.py and ReachableNodes.py"""


class Test_Adjacency(unittest.TestCase):

    """Adjacency matrix -> list testing"""
    def test_mat_to_list(self):
        adj_mat = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        # Verification
        adj_list = [[1, 3], [2], [0], [4], [3], []]   # expected adjacency list
        self.assertEqual(mat_to_list(adj_mat), adj_list)


class Test_ReachableNodes(unittest.TestCase):

    """Adjacency list -> set of reachable nodes testing"""
    def test_reachable(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]

        # Verification
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2, 3, 4})
        self.assertEqual(reachable(adj_list, 3), {3, 4})


if __name__ == '__main__':
    unittest.main()
