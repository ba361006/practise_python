# Coding style

> Check [PEP8](https://peps.python.org/pep-0008/#package-and-module-names) and [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) if something is not mentioned in this document

## Overview
* [Python coding guidelines](#python-coding-guidelines)
* [Naming](#naming)
* [Blank lines](#blank-lines)
* [Whitespaces](#whitespaces)
* [Quotes](#quotes)
* [Comments](#comments)
* [Docstring](#docstring)
* [Indentation](#indentation)
* [Annotation](#annotation)


## Python coding guidelines
|wording   |intent|
|:---------|:----|
|Do        |This standard or practice should be followed in all cases. |
|Do Not    |This standard or practice should never be applied.|
|Should    |This standard or practice should be followed in most cases. |
|Should Not|This standard or practice should not be followed.|
|You can   |This standard or practice can be followed if you want to; it's not necessarily good or bad. |


## Naming
- Do Not declare variables to a meaningless name or abbreviation
- Do the naming like the following examples
    - File
        - module_name
        - package_name
    - Class
        - ClassName
        - public_method
        - __private_method
        - public_variable
        - __private_variable
    - Exception
        - ExceptionName
    - Function
        - function_name
        - function_parameter_name
    - Variable
        - instance_var_name
        - global_var_name
        - local_var_name
    - Constant
        - GLOBAL_CONSTANT_NAME

## Blank lines
- Should separate method implementations with 1 blank line
    ``` python
    def function_1():
        pass

    def function_2():
        pass
    ```

## Whitespaces
- Assignment
    ``` python
    x = 1
    y = 2
    long_variable = 3
    ```
- Immediately inside parentheses, brackets or braces
    ``` python
    spam(ham[1], {eggs: 2})
    ```

- Between a trailing comma and a following close parenthesis
    ``` python
    foo = (0,)
    ```

- Immediately before a comma, semicolon, or colon
    ``` python
    if x == 4:
        print(x, y)
        x, y = y, x
    ```

- Should consider adding whitespace around the operators with the lowest priority, if
operators with different priorities are used
    ``` python
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)
    ```
- Do have spaces around the -> arrow for function annotations
    ``` python
    def munge() -> int: ...
    ```
- Don’t use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter:
    ``` python
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    ```
- When combining an argument annotation with a default value, however, do use spaces around the = sign:
    ``` python
    def munge(sep: str = ""): ...
    def munge(arg: str, sep: str = "", limit=1000): ...
    ```
## Quotes
- Do double-quotes( " ) instead of single-quotes ( ' ) for string 
    ``` python
    print("So printing this sort of message won't raise an error")
    ``` 

## Comments
- Do split long line comments
    ``` python
    # this is a very long line comment so it needs to be splitted 
    # into multiple lines like this
    this_is_a_function()
    ```
- Should Not drown your code in comments. Commenting every line with obvious descriptions of what the code does actually hinders readability and comprehension. Single-line comments should be used when the code is doing something that might not be immediately obvious.
    ``` python
    # Segmentation
    kernel_write = np.ones([5,3], dtype=np.uint8)
    mask_hsv, _ = Tools.hsv(
        input_image=image_in,
        lower=[95,0,130],
        upper=[108,229,209]
    )
    
    # thrshold
    mask_all_wires, _ = Tools.threshold(
        input_image=opening,
        lower=0,
        upper=0
    )
    ```

## Docstring
- Should write docstring for a function if it's too complicated that its name can not descript it well
- You can install a vscode extension "autoDocstring" and set this [file](/documents/docstring/docstring_format.txt) as custom template
- Example
    ``` python
    def function(arg1: str, arg2: "list[str]", kwarg1=1, kwarg="kwarg") -> str:
        """
        Description:
            description for this function

        Arguments:
            [str] arg1:
                description for this arg
            [list[str]] arg2:
                description for this arg

        Keyword Arguments: 
            [int] kwarg1:
                description for this kwarg
            [str] kwarg:
                description for this kwarg

        Return: 
            [str]:
                description for this kwarg

        Edited by: [Year-Month-Day] [Author Name]
        """    
    ```

## Indentation
- Do indent your code blocks with 4 spaces
- If everything fits on the same line, go for it
    ``` python
    # function defining
    def function(arg1: str, arg2: "list[str]") -> str:
        pass
    
    # function calling
    variable = function(arg1="arg1", arg2="arg2")
    ```
- If the trailing parenthesis does not locate at the same line, indent by 4 more spaces to distinguish arguments from the rest, and let it become "one parameter per line"
    ``` python
    # function defining
    def threshold(
            input_image: np.ndarray, 
            lower: int, 
            upper: int, 
            show_image=False, 
            rgb=False
    ) -> np.ndarray:
        pass
    
    # function calling
    variable = threshold(
        input_image=image,
        lower=lower,
        upper=upper,
        show_image=False,
        rgb=False
    )
    ```
- Do have a line break before or after a binary operator
    ``` python
    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest
    )
    ```
- Do have a line break for deeply nested dictionary
``` python
    # invoke a dictionary
    data = (nested_dictionary["layer_1"]
                             ["layer_2"]
                             ["layer_3"]
    )
    
    # assign to a dictionary
    (nested_dictionary["layer_1"]
                      ["layer_2"]
                      ["layer_3"]
    ) = 1
```

## Annotation
- Do type annotation for arguments in every method implementations
    ``` python
    def function(list_of_int: "list[int]"):
        pass
    ```
- Do use spaces around the = sign when combining an argument annotation with a default value, however 
    ``` python
    def function(list_of_int: list = [1,2]):
        pass
    ```
- Do function annotation if it has return value, and indent by a space after colon ( : )
    ``` python
    def sum(arg1: int, arg2: int) -> int:
        return arg1 + arg2
    ```
- You can use an alias for the type if a single name and type is too long.   
  The last resort is to break after the colon and indent by 4.
    ``` python
    def my_function(
        long_variable_name:
            long_module_name.LongTypeName,
    ) -> None:
    ```