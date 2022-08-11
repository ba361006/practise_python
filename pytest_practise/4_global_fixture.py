import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


"""
In this example, the append_first fixture is an autouse fixture.
Because it happens automatically, both tests are affected by it, even though neither test requested it.
That doesn’t mean they can’t be requested though; just that it isn’t necessary.
"""
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]