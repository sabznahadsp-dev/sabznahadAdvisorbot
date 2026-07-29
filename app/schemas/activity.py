from datetime import datetime

from pydantic import BaseModel


class ActivityResponse(BaseModel):

    id: int

    user_id: int

    username: str

    action: str

    description: str

    created_at: datetime


    class Config:
        from_attributes = True