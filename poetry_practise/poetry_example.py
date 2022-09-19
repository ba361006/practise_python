# you might need to reopen vscode to let the linter work
import os
import platform

# This ganna work for both Windows and MacOS user
import pydantic

try:
    import fastapi
    print("fastapi works for MacOS user!")
except ImportError as err:
    print(f"[ImportError]: fastapi will not work for {platform.system()} user")
    
try:
    import win32
    print("win32 works for Windows user!")
except ImportError as err:
    print(f"[ImportError]: win32 will not work for {platform.system()} user")