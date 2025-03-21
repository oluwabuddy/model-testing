from datetime import datetime
from sqlmodel import Field, SQLModel


class AIModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str = Field(index=True)
    status: str = Field(default='PROCESSING')
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=None, nullable=True)