import sys
import python-interview


def test_ping():
    sys.argv = ['foo', '10']
    python-interview.ping()

