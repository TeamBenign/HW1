from calculator import divide, largest
import pytest
division_testdata = [
    (6, 3, 2),
    (10, 0, "division error"),
]
largest_testdata = [
    (list(range(0,10)), 9),
    ([], "empty list"),
]
@pytest.mark.parametrize("a,b,output", division_testdata)
def test_division_numeric(a,b,output):
    assert divide(a,b) == output

@pytest.mark.parametrize("arr,output", largest_testdata)
def test_largest_numeric(arr,output):
    assert largest(arr) == output
