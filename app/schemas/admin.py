from pydantic import BaseModel


class UserAdminResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    phone: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True


class UserRoleUpdate(BaseModel):
    role_id: int


class UserStatusUpdate(BaseModel):
    is_active: bool