import unittest
import sys, os
sys.path.append(os.getcwd())
from main import *


class Test_B(unittest.TestCase):
    def test_B1(self):
        one_to_many = [(s.fio, s.bal, c.name)
                       for c in clas
                       for s in students
                       if s.st_id == c.id]
        self.assertEqual(B1(one_to_many), [('Артамонов', 2, 'физико-математичский'),
                                           ('Балабанов', 5, 'информационно-технологический'),
                                           ('Иваненко', 4, 'социально-экономический'),
                                           ('Иванин', 2, 'социально-экономический'),
                                           ('Иванов', 3, 'социально-экономический'),
                                           ('Петров', 3, 'химико-биологический')])
    def test_B2(self):
        one_to_many = [(s.fio, s.bal, c.name)
                       for c in clas
                       for s in students
                       if s.st_id == c.id]
        self.assertEqual(B2(one_to_many),  [('социально-экономический', 3),
                                            ('физико-математичский', 1),
                                            ('химико-биологический', 1),
                                            ('информационно-технологический', 1)])

    def test_B3(self):
        many_to_many_temp = [(c.name, cs.class_id, cs.st_id)
                             for c in clas
                             for cs in st_cl
                             if c.id == cs.class_id]

        many_to_many = [(s.fio, s.bal, class_name)
                        for class_name, class_id, st_id in many_to_many_temp
                        for s in students if s.id == st_id]
        self.assertEqual(B3(many_to_many), {'Артамонов': ['физико-математичский'],
                                            'Петров': ['химико-биологический'],
                                            'Иванов': ['физико-математичский',
                                                       'социально-экономический'],
                                            'Балабанов': ['социально-экономический',
                                                          'информационно-технологический']})

if __name__ == 'main':
    unittest.main()