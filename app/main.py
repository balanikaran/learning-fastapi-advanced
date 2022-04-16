from typing import Optional
from fastapi import Body, FastAPI, HTTPException, status, Response
from pydantic import BaseModel

app = FastAPI()

# Simple Ping
@app.get("/")
async def root():
    return {
        "message": "Hey! The server is working! :)"
    }


# Generic request body
@app.post("/createPost")
async def createPost(requestPayload: dict = Body(...)):
    return {
        "message": "Your post was created!",
        "requestPayload": requestPayload
    }


# Request payload body
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # default value
    rating: Optional[int] = None  # fully optional value default Null


# request payload with basemodel
@app.post("/createPostWithModel")
async def createPostWithModel(requestPayload: Post):
    print(requestPayload.dict())
    return {
        "message": "Your post was created with Model!",
        "requestPayload": f"title: {requestPayload.title}, content: {requestPayload.content}, published: {requestPayload.published}, rating: {requestPayload.rating}"
    }


# BASIC CRUD!!!
staticUserDb = [
    {
        "firstname": "karan",
        "username": "karan"
    },
    {
        "firstname": "balani",
        "username": "balani"
    }
]


class User(BaseModel):
    firstname: str
    username: str


@app.get("/users")
async def getAllUsers():
    return {
        "data": staticUserDb
    }


@app.get("/usersNotFound")
async def getAllUsers404(response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {
        "data": "not found explicity!!!"
    }


@app.get("/usersNotFoundHTTPException")
async def getAllUsersHttpException():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                        "data": "not found explicitly with http exception!!!"})


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def createUser(user: User):
    staticUserDb.append(user.dict())
    return {
        "data": user.dict()
    }


@app.get("/users/{id}")
async def getUser(id: int):
    return staticUserDb[1]


@app.put("/users/{id}")
async def updateUser(id: int, user: User):
    print(f"id: {id}, user: {user.dict()}")
    return {
        "data": "user updated!!!"
    }


@app.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id: int):
    if len(staticUserDb):
        staticUserDb.pop()

    # Note: for some reason this version of faastapi does not throw error 
    # when we use 204 status with the endpoint but it should throw error
    # because the endpoint with 204 should not return any content
    # to handle this, we use Response Model of fast api

    # return {
    #     "detail": "user deleted!!!"
    # }

    return Response(status_code=status.HTTP_204_NO_CONTENT)