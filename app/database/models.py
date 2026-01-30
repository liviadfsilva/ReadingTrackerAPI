from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class ReadingStatus(str, Enum):
    to_be_read = "to_be_read"
    reading = "reading"
    completed = "completed"
    did_not_finish = "did_not_finish"

class Tracker(BaseModel):
    title: str
    author: str
    status: ReadingStatus = ReadingStatus.reading
    start_reading_date: Optional[str] = Field(default=None, exclude_none=True)
    finish_reading_date: Optional[str] = Field(default=None, exclude_none=True)
    release_date: Optional[str] = Field(default=None, exclude_none=True)
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))