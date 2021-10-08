from sqlalchemy import Column, String, BigInteger, Integer
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base


class BaseLog(Base):
    __abstract__ = True
    id = Column(BigInteger, primary_key=True, nullable=False, index=True, unique=True, autoincrement=True)
    ip_address = Column(String(32), nullable=False)
    date = Column(Integer, default=datetime.utcnow().timestamp())
    description = Column(String(100), default='')
