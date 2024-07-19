# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class AudioStream(BaseModel):
    model_config = get_base_model_config()

    channel_count: int | None = Field(default=None)
    codec: str | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    vendor: str | None = Field(default=None)
