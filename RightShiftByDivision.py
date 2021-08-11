import pytest

def shift_to_right(number,power):
    floor = 2**power
    return number / floor

@pytest.mark.parametrize("number,power,expected",[[80,3,10],[-24,2,-6],[-5,1,-3],[38,0,38],[192,4,12],[4666,6,72],[3777,6,59],[1024,5,32],[-512,10,-1]])
def test(number,power,expected):
    assert shift_to_right(number,power) == expected
