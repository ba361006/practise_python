import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    print()
    print("order function is requested")
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    """
    since this test function request append_first, the result of order(["a"] in this case)
    will be cached
    """
    print()
    print("test_string_only order: ", order)
    print("test_string_only first_entry: ", first_entry)
    print("test_string_only append_first: ", append_first)    

    # Assert
    assert order == [first_entry]

def test_only_order(order):
    """
    test function is independent to each other, so order will be an empty list in this case
    """
    print()
    print("test_only_order order: ", order)