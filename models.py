from typing import Annotated, Optional, Literal
from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel, ConfigDict
from sqlmodel import Field, SQLModel
from enum import Enum
import datetime

class AppointmentStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class User(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(index=True, max_length=64, nullable=False)
    email: str = Field(unique=True, max_length=64, nullable=False)
    password: str = Field(nullable=False)
    active: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    is_staff: Annotated[bool, SkipJsonSchema()] = Field(default=True, nullable=False)
    is_admin: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    last_login: Annotated[datetime.datetime | None, SkipJsonSchema()] = Field(default=None)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class UserLoginCredential(BaseModel):

    email: str
    password: str

class AppointmentSearchInput(BaseModel):

    patient_name: str
    contact_no: str

class AppointmentUpdatedStatus(BaseModel):

    appo_id: str
    new_status: str

class Notification(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    sender_id: Optional[int] = Field(default=None, foreign_key="user.id")
    receiver_id: Optional[int] = Field(default=None, foreign_key="user.id")
    title: str = Field(max_length=64, default="")
    description: str = Field(max_length=128, default="")
    read: bool = Field(default=False)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

#  Appointment
class Appointment(SQLModel, table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    patient_name: str = Field(max_length=64, nullable=False, default="")
    # contacts
    contact_no: str = Field(nullable=False, default="")
    home_contact_no: Optional[str]
    disease: str = Field(max_length=64, nullable=False, default="")
    doctor: int = Field(default=None, foreign_key="doctor.id")
    status: Annotated[AppointmentStatus, SkipJsonSchema()] = Field(default=AppointmentStatus.SCHEDULED)
    appointment_date: datetime.datetime = Field(default=datetime.datetime.now())
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class Speciality(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(max_length=64, nullable=False, default="")
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class SubSpeciality(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(max_length=64, nullable=False, default="")
    speciality: Optional[int] = Field(default=None, foreign_key="speciality.id")
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class Doctor(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    name: str = Field(max_length=64, nullable=False, default="")
    email: str = Field(unique=True, max_length=64, nullable=False, default="")
    contact_no: str = Field(nullable=False)
    speciality: Optional[int] = Field(default="", foreign_key="speciality.id")
    sub_speciality: Optional[int] = Field(default="", foreign_key="subspeciality.id")
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())