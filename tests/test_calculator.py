from src.utils.calculator import add


def test_add():
    """Test the addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
