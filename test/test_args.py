import unittest
import allbase.args as args
from collections import namedtuple
import allbase.base as base


class TestArgs(unittest.TestCase):

    def test_parse(self):

        fix = namedtuple('fix', 'input nums bases valid reason')
        tests = [
            fix(
                input=[],
                nums=None,
                bases=None,
                valid=False,
                reason='no input arguments'
            ),
            fix(
                input=['12'],
                nums=[12],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-f', 'd'],
                nums=[12],
                bases=[base.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['-f', 'd', '12'],
                nums=[12],
                bases=[base.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-f', 'doob'],
                nums=[12],
                bases=[base.dec, base.oct, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['12', '-f', 'doaob'],
                nums=None,
                bases=None,
                valid=False,
                reason="unknown base: 'a'",
            ),
            fix(
                input=['asdf'],
                nums=None,
                bases=None,
                valid=False,
                reason="argument N: invalid _number_from_str value: 'asdf'"
            ),
            fix(
                input=[' '],
                nums=None,
                bases=None,
                valid=False,
                reason="argument N: invalid _number_from_str value: ' '"
            ),
            fix(
                input=['-12'],
                nums=None,
                bases=None,
                valid=False,
                reason="need positive integers, got '-12'"
            ),
            fix(
                input=['12.1'],
                nums=None,
                bases=None,
                valid=False,
                reason="argument N: invalid _number_from_str value: '12.1'"
            ),
            fix(
                input=['12.0'],
                nums=None,
                bases=None,
                valid=False,
                reason="argument N: invalid _number_from_str value: '12.0'"
            ),
            fix(
                input=['0', '1'],
                nums=[0, 1],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['0', '255'],
                nums=[0, 255],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['0', '255', '65536'],
                nums=[0, 255, 65536],
                bases=[base.dec, base.hex, base.oct, base.bin],
                valid=True,
                reason=None
            ),
            fix(
                input=['15', '255', '65535', '-f', 'hd'],
                nums=[15, 255, 65535],
                bases=[base.hex, base.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['-f', 'hd', '15', '255', '65535'],
                nums=[15, 255, 65535],
                bases=[base.hex, base.dec],
                valid=True,
                reason=None
            ),
            fix(
                input=['15', '255', '65535', '-f', 'bo', '1'],
                nums=None,
                bases=None,
                valid=False,
                reason='unrecognized arguments: 1'
            ),
            fix(
                input=['-f', 'bo', '15', '255'],
                nums=[15, 255],
                bases=[base.bin, base.oct],
                valid=True,
                reason=None
            ),
            fix(
                input=['0', '1', '12.0', '15'],
                nums=None,
                bases=None,
                valid=False,
                reason="argument N: invalid _number_from_str value: '12.0'"
            ),
        ]

        for i, t in enumerate(tests):
            nums, bases, valid, reason = args.parse(t.input)

            template = "subtest {0}):\n\tinput = {1!r}\n\t"\
                "nums\n\t\texpected={2}\n\t\tobtained={3}\n\t"\
                "bases\n\t\texpected={4}\n\t\tobtained={5}\n\t"\
                "valid\n\t\texpected={6}\n\t\tobtained={7}\n\t"\
                "reason\n\t\texpected={8!r}\n\t\tobtained={9!r}\n\t"
            comment = template.format(i, t.input,
                                      t.nums, nums,
                                      t.bases, bases,
                                      t.valid, valid,
                                      t.reason, reason)

            self.assertEqual(nums, t.nums, comment)
            self.assertEqual(bases, t.bases, comment)
            self.assertEqual(valid, t.valid, comment)
            self.assertEqual(reason, t.reason, comment)
