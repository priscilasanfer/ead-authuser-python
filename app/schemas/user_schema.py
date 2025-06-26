from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.models.enums.user_status import UserStatus
from app.models.enums.user_type import UserType


class UserBase(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    password: str
    full_name: str
    user_status: UserStatus
    user_type: UserType
    phone_number: Optional[str] = None
    cpf: Optional[str] = None
    image_url: Optional[str] = None
    creation_date: datetime
    last_update_date: datetime
