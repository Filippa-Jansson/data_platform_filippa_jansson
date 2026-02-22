#importer från user.py filen

from typing import Union

from fastapi import FastAPI, status

from user import UserSchema, UserSchemaResponse

from fox import FoxSchema

import requests

#En lista skapad för user.py
userList: list[UserSchema] = [
    UserSchema(username="Benny", password="123"),
]


app = FastAPI(title= "My first API App")

#@app.get hjälper när man söker http adress
@app.get("/")
def root(test: str):
    return{"Hello": "World"}

@app.get("/items/{item_id}") # localhost:8000/items/249 <- "här måste finnas något"
def get_item(item_id: int, color: Union[str, None] = None):
    return{"item_id": item_id, "color": color} #returnerar dictonaryn så att den används

@app.get("/users", response_model=list[UserSchemaResponse])
def get_users() -> list [UserSchemaResponse]: 
    return userList

@app.post("/userz", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def post_users(user: UserSchema) -> UserSchema:
    userList.append(user)
    return user

@app.get("/fox",response_model=FoxSchema)
def get_fox(): 
    response = requests.get("https://randomfox.ca/floof")
    result_json=response.json()
    print(f"DEBUGGING {response}")
    fox = FoxSchema(**result_json)

    return fox