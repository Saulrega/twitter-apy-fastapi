# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List


# Pydantic
from pydantic import BaseModel, EmailStr, fields
from pydantic import Field

# FastAPI
from fastapi import FastAPI, status


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
      max_length=50
   )
   last_name: str = Field(
      ...,
      min_length=1,
      max_length=50
   )
   birth_date: Optional[date] = Field(default=None)


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
def signup():
   pass


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