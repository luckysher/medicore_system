from typing import Annotated, Optional
from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
import datetime

class User(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(index=True, max_length=64, nullable=False)
    email: str = Field(unique=True, max_length=64, nullable=False)
    password: str = Field(nullable=False)
    active: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    is_staff: Annotated[bool, SkipJsonSchema()] = Field(default=True, nullable=False)
    is_admin: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())
    last_login: Annotated[datetime.datetime | None, SkipJsonSchema()] = Field(default=None)


class UserLoginCredential(BaseModel):

    email: str
    password: str

class Notification(SQLModel, table=True):
    id: int = Field(primary_key=True)
    sender_id: Optional[int] = Field(default=None, foreign_key="user.id")
    receiver_id: Optional[int] = Field(default=None, foreign_key="user.id")
    title: str = Field(max_length=64, default="")
    description: str = Field(max_length=128, default="")
    read: bool = Field(default=False)
    created_at: datetime.datetime = Field(default=datetime.datetime.now())

