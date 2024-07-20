# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BaseLiveStreamingDetails(BaseModel):
    model_config = get_base_model_config()

    actual_start_time: datetime | str | None = Field(default=None)
    actual_end_time: datetime | str | None = Field(default=None)
    scheduled_start_time: datetime | str | None = Field(default=None)
    scheduled_end_time: datetime | str | None = Field(default=None)
    concurrent_viewers: int | None = Field(default=None)
    active_live_chat_id: str | None = Field(default=None)
