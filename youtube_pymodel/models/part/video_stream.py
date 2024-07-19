# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class VideoStream(BaseModel):
    model_config = get_base_model_config()

    width_pixels: int | None = Field(default=None)
    height_pixels: int | None = Field(default=None)
    frame_rate_fps: float | None = Field(default=None)
    aspect_ratio: float | None = Field(default=None)
    codec: str | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    rotation: str | None = Field(default=None)
    vendor: str | None = Field(default=None)
