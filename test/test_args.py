import unittest
import allbase.args as args
from collections import namedtuple
from allbase.base import Bases


class TestArgs(unittest.TestCase):

    def test_parse(self):

        fix = namedtuple('fix', 'input num bases valid reason')
        tests = [
            fix(
                input=[],
                num=None,
                bases=None,
                valid=False,
                reason='no input arguments'
            ),
            fix(
                input=['12'],
                num=12,
                bases=[Bases.dec, Bases.hex, Bases.oct, Bases.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-b', 'd'],
                num=12,
                bases=[Bases.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-b', 'doob'],
                num=12,
                bases=[Bases.dec, Bases.oct, Bases.oct, Bases.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-b', 'doaob'],
                num=12,
                bases=None,
                valid=False,
                reason="unknown base: 'a'",
            ),
        ]

        for i, t in enumerate(tests):
            num, bases, valid, reason = args.parse(t.input)

            template = "subtest {0}):\n\tinput = {1!r}\n\t"\
                "num\n\t\texpected={2}\n\t\tobtained={3}\n\t"\
                "bases\n\t\texpected={4}\n\t\tobtained={5}\n\t"\
                "valid\n\t\texpected={6}\n\t\tobtained={7}\n\t"\
                "reason\n\t\texpected={8!r}\n\t\tobtained={9!r}\n\t"
            comment = template.format(i, t.input,
                                      t.num, num,
                                      t.bases, bases,
                                      t.valid, valid,
                                      t.reason, reason)

            self.assertEqual(num, t.num, comment)
            self.assertEqual(bases, t.bases, comment)
            self.assertEqual(valid, t.valid, comment)
            self.assertEqual(reason, t.reason, comment)
