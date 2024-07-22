# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class SharedContentStream(BaseModel):
    model_config = get_base_model_config()

    channel_count: int | None = Field(default=None)
    codec: str | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    vendor: str | None = Field(default=None)


class AudioStream(SharedContentStream):
    model_config = get_base_model_config()

    channel_count: int | None = Field(default=None)


class VideoStream(SharedContentStream):
    model_config = get_base_model_config()

    width_pixels: int | None = Field(default=None)
    height_pixels: int | None = Field(default=None)
    frame_rate_fps: float | None = Field(default=None)
    aspect_ratio: float | None = Field(default=None)
    rotation: str | None = Field(default=None)
