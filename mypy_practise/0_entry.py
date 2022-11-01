from typing import List


def greet_all(names: List[str]) -> None:
    for name in names:
        print("Hello " + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)  # Ok!
greet_all(ages)  # Error due to incompatible types

# to check this file, run mypy mypy_practise/0_entry.py
# to check mypy_practise folder, run mypy mypy_practise
# to check subdirectory folder, run mypy mypy_practise/sub_directory/*