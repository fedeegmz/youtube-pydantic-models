# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class BaseStatus(BaseModel):
    model_config = get_base_model_config()

    privacy_status: str | None = Field(default=None)


class SharedStatus(BaseStatus):
    model_config = get_base_model_config()

    made_for_kids: bool | None = Field(default=None)
    self_declared_made_for_kids: bool | None = Field(default=None)


class ChannelStatus(SharedStatus):
    model_config = get_base_model_config()

    is_linked: bool | None = Field(default=None)
    long_uploads_status: str | None = Field(default=None)


class VideoStatus(SharedStatus):
    model_config = get_base_model_config()

    upload_status: str | None = Field(default=None)
    failure_reason: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    publish_at: datetime | str | None = Field(default=None)
    license: str | None = Field(default=None)
    embeddable: bool | None = Field(default=None)
    public_stats_viewable: bool | None = Field(default=None)
