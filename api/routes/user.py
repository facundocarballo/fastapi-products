from fastapi import APIRouter, HTTPException
from domain.user import User
from database.connection import create_local_connection
from ..handlers.passwords import hash_password
from schemas.user import userEntity
from bson import ObjectId

user_routes = APIRouter()
mongo_client = create_local_connection()
db = mongo_client["ScalablePath"]
user_collection = db["User"]

@user_routes.post("/user")
async def create_user(user: User):
    user.password = hash_password(user.password)
    try:
        user_id = user_collection.insert_one(dict(user)).inserted_id
        new_user = user_collection.find_one({"_id": user_id})
        return {
            "message": "User created successfully.",
            "user": userEntity(new_user)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@user_routes.put("/user")
def update_user(user: User):
    try:
        user_collection.update_one({"_id": ObjectId(user._id)}, {
            "$set": dict(user)
        })
        return {
            "message": "User updated succesfully.",
            "user": userEntity(user)
        }
    except Exception as e:
        return {
            "messsage": "Error trying to update the user. " + str(e)
        }

@user_routes.patch("/user")
def update_patch_user():
    return {
        "messsage": "Update patch user"
    }

@user_routes.get("/user")
def get_user():
    return {
        "messsage": "Get user"
    }

@user_routes.delete("/user")
def delete_user():
    return {
        "messsage": "Delete user"
    }