from unittest.mock import Mock
import json

# use Mock to replace json
json = Mock()


# mock will dynamically create another instance since dumps method is called
json.dumps({"hello":"world"})


# to prove that json.dumps creates a new instance
print("json: ", id(json))
print("json.dump: ", id(json.dumps))


# to show the built-in methods for Mock
print()
print("built-in methods: \n", dir(json))


# returning None from assert indicates True
print()
print(json.dumps.assert_called()) # whether json.dumps has been called
print(json.dumps.assert_called_once()) # whether json.dumps has been called once
print(json.dumps.call_args) # return the args from the last call of json.dumps
print(json.dumps.call_count) # return the times that json.dumps has been called


# this will raise an error since we call json.dumps twice
try:
    json.dumps({"second":"call"})
    json.dumps.assert_called_once()
except Exception as err:
    print()
    print("second called error: ", err)


# this show the calls of Mock object(json) from the beginning
json.some_other_methods()
print()
print(json.method_calls)