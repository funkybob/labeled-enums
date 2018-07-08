from unittest import TestCase

from lenum import LabeledEnum


class STATUS(LabeledEnum):
    CLOSED = 0
    NEW = 1
    PENDING = 2, 'Process Pending'
    FAILED = -1, 'Processing Failed'


class TestLenum(TestCase):

    def test_lookup(self):
        self.assertEqual(STATUS.CLOSED, 0)
        self.assertEqual(STATUS.FAILED, -1)

    def test_reverse(self):
        self.assertEqual(STATUS.for_label('Closed'), 0)
        self.assertEqual(STATUS.for_label('Processing Failed'), -1)

    def test_label(self):
        self.assertEqual(STATUS[0], 'Closed')
        self.assertEqual(STATUS[-1], 'Processing Failed'),

    def test_iterate(self):
        self.assertEqual(list(STATUS), [
            (0, 'Closed'),
            (1, 'New'),
            (2, 'Process Pending'),
            (-1, 'Processing Failed'),
        ])

    def test_iter_callable(self):
        '''
        Handles how Django's Form.field choices treats callabls
        '''
        self.assertEqual(list(STATUS()), [
            (0, 'Closed'),
            (1, 'New'),
            (2, 'Process Pending'),
            (-1, 'Processing Failed'),
        ])

    def test_names(self):
        self.assertEqual(STATUS.names, ('CLOSED', 'NEW', 'PENDING', 'FAILED',))

    def test_setattr(self):
        with self.assertRaises(AttributeError):
            STATUS.OLD = 3

    def test_setattr_names(self):
        with self.assertRaises(AttributeError):
            STATUS.names = {}

    def test_names_mangle(self):
        with self.assertRaises(AttributeError):
            STATUS.names.add('foo')
