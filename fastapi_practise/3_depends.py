from typing import Optional
import fastapi

# python3 -m uvicorn fastapi_practise.3_depends:app --reload

app = fastapi.FastAPI()


class Test:
    def __init__(self, arg):
        print("Test init arg: ", arg)
        self.arg = arg
    
    def __call__(self, arg):
        print("Test call arg: ", arg)
        return 1

def func(arg, depend: Optional[int] = fastapi.Depends(Test)):
    print("func arg: ", arg)
    depend(arg)

@app.get("/")
async def root(arg = fastapi.Depends(func)):
    return {"message": arg}

"""
1. when instantiating route function(root), callable object(func, Test) will be 
assigned(dependency injection) to arg and depend respectively

2. when api is called, func and Test.__init__ will both be called with arg given by user

3. so firstly "Test init arg: {user_arg}" will be printed, then "func arg: {user_arg}",
I guess this is because Test has been injected to fastapi.Depends ealier than func
(see the line number of them)

4. after "func arg: {user_arg}" is printed, depend(arg) is called so user_arg will be sent
to Test.__call__

5. end

Note: if depend(arg) is never invoked, then Test.__call__ will never be called
"""