import pytest
# this function return if the two nodes are adjancent with build Matrix
# Params ( Matrix, nodeOne, nodeTwo)


def is_adjacent(matrix, nodeOne, nodeTwo):
    if(matrix[nodeOne][nodeTwo] == 1):
        return True
    return False

@pytest.fixture
def matrix():
    matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
    return matrix

@pytest.mark.parametrize(
        "nodeOne, nodeTwo, boolean",
        [[0,1,True],[0,2,False],[2,1,True]])
def test_one(matrix,nodeOne,nodeTwo,boolean):
    assert is_adjacent(matrix,nodeOne,nodeTwo) == boolean




