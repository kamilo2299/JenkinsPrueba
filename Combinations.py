import pytest

def combinations(lst):
    result = 1;
    for i in lst:
        if i != 0:
            result *= i
    return result

@pytest.mark.parametrize(
        "lst,expected",
        [[[2,1],2],[[2,3],6],[[3,5],15],[[5,6,7],210],[[5,5,5,5],625],[[3,6,9],162],[[2,3,4,5,6,7,8,9,10],3628800],[[4,5,6],120],[[5,6,7,8],1680],[[6,7,0],42]])

def test(lst,expected):
    assert combinations(lst) == expected
