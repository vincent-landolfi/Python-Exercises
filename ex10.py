from reading import *
from database import *
from squeal import *
import unittest


class TestCartesian(unittest.TestCase):

    def test_num_rows(self):
        d1 = {'test1': [1, 2, 3, 4], 'test3': [1, 2, 3, 3]}
        d2 = {'test2': [1, 2, 3]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        keys = list(result_dict.keys())
        rows = len(result_dict[keys[0]])
        self.assertEqual(rows, 12, "Incorrect number of rows")

    def test_num_columns(self):
        d1 = {'test1': [1, 2, 3, 4], 'test3': [1, 2, 3, 3]}
        d2 = {'test2': [1, 2, 3]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        keys = list(result_dict.keys())
        self.assertEqual(len(keys), 3, "Incorrect number of columns")

    def test_when_first_has_more_rows(self):
        d1 = {'test1': [1, 2, 3, 4]}
        d2 = {'test2': [1, 2, 3]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'test1': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
                         'test2': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]}
        self.assertEqual(result_dict, expected_dict,
                         "Incorrect when first table has more" +
                         "rows than second table")

    def test_when_second_has_more_rows(self):
        d1 = {'test1': [1, 2, 3]}
        d2 = {'test2': [1, 2, 3, 4]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'test1': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
                         'test2': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]}
        self.assertEqual(result_dict, expected_dict,
                         "Incorrect when first table has" +
                         "more rows than second table")

    def test_when_first_has_more_columns(self):
        d1 = {'test1': [1, 2, 3], 'test3': [4, 5, 6]}
        d2 = {'test2': [1, 2, 3, 4]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'test1': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
                         'test2': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
                         'test3': [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]}
        self.assertEqual(result_dict, expected_dict,
                         "Incorrect when first table has more columns")

    def test_when_second_has_more_columns(self):
        d1 = {'test1': [1, 2, 3]}
        d2 = {'test2': [1, 2, 3, 4], 'test3': [5, 6, 7, 8]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'test1': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
                         'test2': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
                         'test3': [5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8]}
        self.assertEqual(result_dict, expected_dict,
                         "Incorrect when first table has more columns")

    def test_blank_table_first(self):
        d1 = {'test1': []}
        d2 = {'test2': [1, 2, 3], 'test6': [1, 24, 4]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'test1': [], 'test2': [], 'test6': []}
        self.assertEqual(result_dict, expected_dict,
                         "Doesn't work with blank lists as values," +
                         "in the first table")

    def test_blank_table_second(self):
        d1 = {'test1': [1, 2, 3, 4], 'test3': [1, 2, 3, 3]}
        d2 = {'test2': []}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'test1': [], 'test2': [], 'test3': []}
        self.assertEqual(result_dict, expected_dict,
                         "Doesn't work with blank lists as values," +
                         "in the second table")

    def test_example(self):
        d1 = {'m.year': ['a', 'b', 'c'], 'm.title': ['d', 'e', 'f'],
              'm.studio': ['g', 'h', 'i'], 'm.gross': ['j', 'k', 'l']}
        d2 = {'o.year': ['c', 'b', 'a', 'a'],
              'o.category': ['m', 'n', 'n', 'o'],
              'o.title': ['f', 'e', 'd', 'd']}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {'m.year': ['a', 'a', 'a', 'a',
                         'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c'],
                         'm.title': ['d', 'd', 'd', 'd',
                                     'e', 'e', 'e', 'e', 'f', 'f', 'f', 'f'],
                         'm.studio': ['g', 'g', 'g', 'g',
                                      'h', 'h', 'h', 'h', 'i', 'i', 'i', 'i'],
                         'm.gross': ['j', 'j', 'j', 'j',
                                     'k', 'k', 'k', 'k', 'l', 'l', 'l', 'l'],
                         'o.year': ['c', 'b', 'a', 'a',
                                    'c', 'b', 'a', 'a', 'c', 'b', 'a', 'a'],
                         'o.category': ['m', 'n', 'n', 'o', 'm',
                                        'n', 'n', 'o', 'm', 'n', 'n', 'o'],
                         'o.title': ['f', 'e', 'd', 'd', 'f',
                                     'e', 'd', 'd', 'f', 'e', 'd', 'd']}
        self.assertEqual(result_dict, expected_dict,
                         "Doesn't make the proper cartesian product")


if __name__ == '__main__':
    unittest.main(exit=False)