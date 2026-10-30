import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID, JSONB

from database import Base


class ExtractionStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"


class Extraction(Base):
    __tablename__ = "extractions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    status = Column(SQLEnum(ExtractionStatus), default=ExtractionStatus.pending, nullable=False)
    extracted_data = Column(JSONB, nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)