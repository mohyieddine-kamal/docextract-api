from pydantic import BaseModel
import uuid
from models import ExtractionStatus
from datetime import datetime
from typing import Optional
from typing import List
from enum import Enum

class DatabaseStatus(str, Enum):
    ok = "ok"
    unreachable = "unreachable"



class ExtractionOut(BaseModel):
    id:uuid.UUID
    filename: str
    content_type: str
    status: ExtractionStatus
    extracted_data: Optional[dict] = None
    error_message: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class ExtractionListOut(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[ExtractionOut]

class HealthOut(BaseModel):
    status: str
    database: DatabaseStatus