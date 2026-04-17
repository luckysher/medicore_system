from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import Optional
from server_base import *
from db_connection_manager import SessionDep
from models import *
from utils import PasswordManager
from sqlmodel import select
from validator import user_input_validator


@app.get("/auth/users/{user_id}")
def get_user_with_with_id(user_id:int, session: SessionDep):
    """
    API get request for fetching user
    """
    try:
        user = session.get(User, user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail="Unknown error occurred")

