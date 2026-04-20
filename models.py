from typing import Annotated, Optional
from pydantic.json_schema import SkipJsonSchema
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Enum
import datetime

class AppointmentStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class BaseSqlModel(SQLModel, table=True):
    id: Annotated[int, SkipJsonSchema()] = Field(primary_key=True)
    created_at: Annotated[datetime.datetime, SkipJsonSchema()] = Field(default=datetime.datetime.now())

class User(BaseSqlModel):
    name: str = Field(index=True, max_length=64, nullable=False)
    email: str = Field(unique=True, max_length=64, nullable=False)
    password: str = Field(nullable=False)
    active: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    is_staff: Annotated[bool, SkipJsonSchema()] = Field(default=True, nullable=False)
    is_admin: Annotated[bool, SkipJsonSchema()] = Field(default=False, nullable=False)
    last_login: Annotated[datetime.datetime | None, SkipJsonSchema()] = Field(default=None)


class UserLoginCredential(BaseModel):

    email: str
    password: str

class Notification(BaseSqlModel):
    sender_id: Optional[int] = Field(default=None, foreign_key="user.id")
    receiver_id: Optional[int] = Field(default=None, foreign_key="user.id")
    title: str = Field(max_length=64, default="")
    description: str = Field(max_length=128, default="")
    read: bool = Field(default=False)

#  Appointment
class Appointment(BaseSqlModel):
    patient_name: str = Field(max_length=64, nullable=False, default="")
    # contacts
    contact_no: int = Field(nullable=False)
    home_contact_no: int = Field(nullable=False)
    disease: str = Field(max_length=64, nullable=False, default="")
    doctor: Optional[int] = Field(default=None, foreign_key="doctor.id")
    status: AppointmentStatus = Field(default=AppointmentStatus.SCHEDULED, nullable=False)
