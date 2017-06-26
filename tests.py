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

    def test_compat(self):
        self.assertEqual(STATUS(0), 0)
        self.assertEqual(STATUS(1), 1)
        self.assertIsNone(STATUS(99))

    def test_reverse(self):
        self.assertEqual(STATUS.label('Closed'), 0)
        self.assertEqual(STATUS.label('Processing Failed'), -1)

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
