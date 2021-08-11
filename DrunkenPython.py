import pytest


def int_to_str(number):
    return str(number)

def str_to_int(string):
    return int(string)

@pytest.mark.parametrize("integer,expected",[[4,"4"],[65,"65"],[29348,"29348"],[49583908545,"49583908545"]])
def test_int_to_str(integer, expected):
    assert int_to_str(integer) == expected


@pytest.mark.parametrize("string,expected",[["4",4],["65",65],["29348",29348],["49583908545",49583908545]])
def test_str_to_int(string, expected):
    assert str_to_int(string) == expected




