# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BaseRecordingDetails(BaseModel):
    model_config = get_base_model_config()

    recording_date: datetime | str | None = Field(default=None)
