from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    telegram_id = Column(Integer, unique=True, nullable=False)

    first_name = Column(String(100))
    last_name = Column(String(100))

    phone = Column(String(20))

    province = Column(String(100))
    city = Column(String(100))

    job = Column(String(100))
    activity = Column(String(100))

    address = Column(String(500))

    postal_code = Column(String(20))