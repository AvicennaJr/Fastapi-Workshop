from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def greet():
    "This endpoint is for greeting"
    return {"message": "Hello Guys, welcome"}


@app.get("/about")
def about():
    "Returns information about me"
    return {"message": "I am a software developer"}
