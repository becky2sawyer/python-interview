import sys
import python_interview


def test_ping():
    sys.argv = ['foo', '10']
    python_interview.ping()

