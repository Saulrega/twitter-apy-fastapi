# Python
import json
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List


# Pydantic
from pydantic import BaseModel, EmailStr, fields
from pydantic import Field

# FastAPI
from fastapi import FastAPI, status, Body


app = FastAPI()


#Models

class UserBase(BaseModel):
   user_id: UUID = Field(...,)
   email: EmailStr = Field(..., )

class UserLogin(UserBase):
   password: str = Field(
      ...,
      min_length=8
   )

class User(UserBase):
   first_name: str = Field(
      ...,
      min_length=1,
      max_length=50,
      example="Saul"
   )
   last_name: str = Field(
      ...,
      min_length=1,
      max_length=50,
      example="Perez"
   )
   birth_date: Optional[date] = Field(default=None)

class UserRegister(User, UserLogin):
   pass

class Tweet(BaseModel):
   tweet_id: UUID = Field(...)
   content: str = Field(
      ...,
      min_length=1,
      max_length=290,
   )
   created_at: datetime = Field(default=datetime.now())
   update_at: Optional[datetime] = Field(default=None)
   by: User = Field(...)


# Path Operations 



## Auth

### Register a user
@app.post(
   path="/auth/signup",
   response_model=User,
   status_code=status.HTTP_201_CREATED,
   summary="Register a User",
   tags=["Auth", "Users"]
)
def signup(user: UserRegister = Body(...)):
   """
   Singup a user

   This path operation register a user in the app

   Parameters:
      -Request body parameter
         -user: UserRegister


   Returns a json with the basic user information:
      -user_id: UUID
      -email: Emailstr
      -first_name: str
      -last_name: str
      -birth_date: date
   """
   with open("users.json", "r+", encoding="utf-8") as f:
      results = json.loads(f.read())
      user_dict = user.dict()
      user_dict["user_id"] = str(user_dict["user_id"])
      user_dict["birth_date"] = str(user_dict["birth_date"])
      results.append(user_dict)
      f.seek(0)
      f.write(json.dumps(results))
      return user


### Login a user
@app.post(
   path="/auth/login",
   response_model=User,
   status_code=status.HTTP_200_OK,
   summary="Login a User",
   tags=["Auth", "Users"]
)
def login():
   pass


## Users

### Show all user
@app.get(
   path="/users",
   response_model=List[User],
   status_code=status.HTTP_200_OK,
   summary="Show all users",
   tags=["Users"]
)
def show_all_users():
   pass


### Delete a user
@app.get(
   path="/users/{user_id}",
   response_model=User,
   status_code=status.HTTP_200_OK,
   summary="Show a User",
   tags=["Users"]
)
def delete_a_user():
   pass


### Update a user
@app.put(
   path="/users/{user_id}/update",
   response_model=User,
   status_code=status.HTTP_200_OK,
   summary="Update a User",
   tags=["Users"]
)
def update_a_user():
   pass




# Tweets

### Show all tweets
@app.get(
   path="/",
   response_model=List[Tweet],
   status_code=status.HTTP_200_OK,
   summary="Show all tweets",
   tags=["Tweets"]
)
def home():
   return {"Twitter API": "Working!!"}


### Post a tweet
@app.post(
   path="/post",
   response_model=Tweet,
   status_code=status.HTTP_201_CREATED,
   summary="Post a Tweet",
   tags=["Tweets"]
)
def post_a_tweet():
   pass


### Show a tweet
@app.get(
   path="/tweets/{tweet_id}",
   response_model=Tweet,
   status_code=status.HTTP_200_OK,
   summary="Show a Tweet",
   tags=["Tweets"]
)
def show_a_tweet():
   pass


### Delete a tweet
@app.delete(
   path="/tweets/{tweet_id}",
   response_model=Tweet,
   status_code=status.HTTP_200_OK,
   summary="Delete a Tweet",
   tags=["Tweets"]
)
def delete_a_tweet():
   pass


### Update a tweets
@app.delete(
   path="/tweets/{tweet_id}",
   response_model=Tweet,
   status_code=status.HTTP_200_OK,
   summary="Update a Tweet",
   tags=["Tweets"]
)
def update_a_tweet():
   pass