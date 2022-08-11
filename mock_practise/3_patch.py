from unittest.mock import patch
"""
patch has two and three argument forms

the three argument form takes the object to be patched, the attribute name
and the object to replace

when calling with two argument form you omit the replacement object,
and a MagicMock / AsyncMock is created for you and passed in as an extra
argument to the decorated function(the extra argument will be the last argument)
"""

class SomeClass:
    def hello(self, arg):
        print("hello: ", arg)


def patch_1_with_object():
    # patcher mocks the method "hello" from SomeClass
    patcher = patch.object(target=SomeClass, attribute="hello")
    
    # invoking start method to get the mocked object
    mock_hello = patcher.start()
    
    # verify the hello method has been called with argument 3
    SomeClass().hello(3)
    try:
        mock_hello.assert_called_with(2)
    except AssertionError as err:
        print("### from patch_1_with_object ###")
        print(
            "an AssertionError has been raised according to "+
            "SomeClass().hello has been called with unexpected "+
            "value. (expected to be 2, but 3 was given)"
        )
        print()


def patch_2_with_context_manager():
    foo = {'key': 'value'}
    original = foo.copy()
    
    # foo with newkey/newvalue would be undone after exiting the scope
    with patch.dict(
        in_dict=foo, 
        values={'newkey': 'newvalue'}, 
        clear=True
    ):
        assert foo == {'newkey': 'newvalue'}

    # verify foo hasn't been changed by patch
    assert foo == original
    
    
def patch_3_with_decorator():
    # target should be a string in the form "package.module.ClassName"
    # the mocked_object will be imported with the last argument in the
    # decorated function
    @patch(target='__main__.SomeClass')
    def function(first, second, third, mocked_object):
        print("arguments: ", first, second, third)
        print("mocked_object: ", mocked_object)
        print("mocked_object is SomeClass: ", mocked_object is SomeClass)
    print("### from patch_3_with_decorator ###")
    function(1,2,3)


def patch_4_with_assertion():
    # this one is equivalent to patch_1_with_object but in decorator form
    # and expected value
    @patch.object(SomeClass, 'hello')
    def assertion_test(mock_hello):
        SomeClass().hello(3)
        mock_hello.assert_called_with(3)

    assertion_test()

if __name__ == "__main__":
    patch_1_with_object()
    patch_2_with_context_manager()
    patch_3_with_decorator()
    patch_4_with_assertion()


