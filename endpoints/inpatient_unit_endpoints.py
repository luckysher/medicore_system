import datetime

from fastapi.encoders import jsonable_encoder
from server_base import *
from db_connection_manager import SessionDep
from models import *
from utils import Tags
from sqlmodel import select, or_
#from validator import 

# ADT (Admission, Discharge and Transfer)
@app.post("/admissions", status_code=status.HTTP_201_CREATED)
async def admit_new_patient():
    """
    API post request for admitting a new patient
    """
    pass

@app.post("/discharge", status_code=status.HTTP_201_CREATED)
async def discharge_patient():
    """
    API post request for discharging a patient
    """
    pass

@app.post("/transfer", status_code=status.HTTP_201_CREATED)
async def transfer_patient():
    """
    API post request for transferring a patient from one unit to another unit
    """
    pass