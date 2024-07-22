# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class BaseStatistics(BaseModel):
    model_config = get_base_model_config()

    view_count: str | None = Field(default=None)


class ChannelStatistics(BaseStatistics):
    model_config = get_base_model_config()

    subscriber_count: str | None = Field(default=None)
    hidden_subscriber_count: bool | None = Field(default=None)
    video_count: str | None = Field(default=None)


class VideoStatistics(BaseStatistics):
    model_config = get_base_model_config()

    like_count: str | None = Field(default=None)
    dislike_count: str | None = Field(default=None)
    favorite_count: str | None = Field(default=None)
    comment_count: str | None = Field(default=None)
