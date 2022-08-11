from unittest.mock import Mock

# side_effect allows you to do something else when calling the configured mock
def side_effects():
    try:
        exception_mock = Mock(side_effect=Exception("exception raised"))
        exception_mock()
    except Exception as error:
        print("exceptino mock raises this: ", error)

    print_mock = Mock(side_effect=lambda: print("hi there"))
    print_mock()


def name():
    # assign when instantiating
    ori_mock = Mock()
    name_mock = Mock(name="self-named mock")
    print("ori_mock: ", ori_mock)
    print("name_mock: ", name_mock)
    
    # note that name can't be assigned after .__init__()
    # it only makes name a mocked method
    after_init_mock = Mock()
    after_init_mock.name = "self-named mock"
    print("after_init_mock: ", after_init_mock.name)

if __name__ == "__main__":
    side_effects()
    
    print()
    name()