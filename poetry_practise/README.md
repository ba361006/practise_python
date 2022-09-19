# Poetry
It's an dependency management application for Python.
It would limit everything to a single configuration file to do: dependency management, packaging and publishing.
Also, it supports cross platform dependency management.

## To let poetry_example.py works
1. get in poetry_practise as root directory
2. *(This step is optional)* run `poetry config virtualenvs.in-project true` (go check the meaning of this command below) 
3. run `poetry install`
4. now poetry should finish the environment setup
5. execute poetry_example.py

## pyproject.toml
It's a file that contains the configuration, dependency packages, etc.

- cross platform support:  
    | platform | string for sys_platform | 
    |:--------:|:-----------------------:|
    | Windows  |          win32          |
    |  Linux   |          linux          |
    |  MacOS   |          darwin         |
    ```
    [tool.poetry.dependencies]
    python = ">=3.9,<3.10"
    
    # pydantic will be installed to .venv for every user
    pydantic = "*"

    # pywin32 will only be installed to .venv for Windows users
    pywin32 = [{ version = "*", markers = "sys_platform=='win32'"}]

    # fastapi will only be installed to .venv for MacOS users
    fastapi = [{version="*", markers="sys_platform=='darwin'"}]
    ```

## command line
- `poetry config virtualenvs.in-project true`
    - ask poetry to put the virtualenv file(`.venv`) in the current directory, otherwise `.venv` will be placed at somewhere else(for windows, it will be placed at `C:\Users\ba361\AppData\Local\pypoetry\Cache\virtualenvs`)
    - add `--local` to create a `poetry.toml` file which asks poetry to put `.venv` at the current directory(this feature is only valid  in the current directory).

- `poetry init`
    - to create a `pyproject.toml` file

- `poetry install`
    - to create virtualenv and the dependency packages
    - this command only needs to be called once

- `poetry update`
    - to install/remove the packages/setting that have been modified in pyproject.toml
