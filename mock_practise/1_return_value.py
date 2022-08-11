import datetime
from unittest.mock import Mock


def return_value_0():
    test_instance = Mock()
    
    # return_value is a method from Mock instance
    test_instance.method.return_value = "return!"
    
    # it's an method of test_instance
    print("method: ", test_instance.method)
    
    # it's the return value of the method
    print("method(): ", test_instance.method())

def return_value_1():
    """
    sometimes we don't need to test something like this example,
    but we don't want our test to be fail just because today is not 
    a weekday, it ganna make the test be unpredictable
    
    so here we save both weekday and non-weekday data
    and put it to the test, and the result will be absolutely the same
    as it should be
    """
    # Save a couple of test days
    tuesday = datetime.datetime(year=2019, month=1, day=1)
    saturday = datetime.datetime(year=2019, month=1, day=5)

    # Mock datetime to control today's date
    datetime_ = Mock()

    def is_weekday():
        today = datetime.datetime.today()
        # Python's datetime library treats Monday as 0 and Sunday as 6
        return (0 <= today.weekday() < 5)

    # Mock .today() to return Tuesday
    datetime_.datetime.today.return_value = tuesday
    
    # Test Tuesday is a weekday
    assert is_weekday()
    
    # Mock .today() to return Saturday
    datetime_.datetime.today.return_value = saturday
    
    # Test Saturday is not a weekday
    assert not is_weekday()

if __name__ == "__main__":
    return_value_0()
    # return_value_1()