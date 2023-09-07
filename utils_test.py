from itertools import chain
from utils import Utils

def test_reversed():
    int_test = range(1, 11)
    str_test = (str(x) for x in range(1, 11))
    float_test = (float(x) for x in range(1, 11))

    for i in chain(int_test, str_test, float_test):
        val = Utils.reversed(i)
        print(val)


if __name__ == "__main__":
    test_reversed()
