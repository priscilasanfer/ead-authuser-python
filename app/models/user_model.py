import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, String
from sqlalchemy.dialects.postgresql import UUID

from app.models import Base
from app.models.enums.user_status import UserStatus
from app.models.enums.user_type import UserType


class UserModel(Base):
    __tablename__ = "tb_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)
    user_status = Column(Enum(UserStatus), nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    phone_number = Column(String(20), nullable=True)
    cpf = Column(String(20), nullable=True)
    image_url = Column(String, nullable=True)
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    last_update_date = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
