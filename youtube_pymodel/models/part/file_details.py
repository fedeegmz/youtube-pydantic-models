# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.part.video_stream import VideoStream
from models.part.audio_stream import AudioStream


class FileDetails(BaseModel):
    model_config = get_base_model_config()

    file_name: str | None = Field(default=None)
    file_size: int | None = Field(default=None)
    file_type: str | None = Field(default=None)
    container: str | None = Field(default=None)
    video_streams: list[VideoStream | None] = Field(default=[])
    audio_streams: list[AudioStream | None] = Field(default=[])
    duration_ms: int | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    creation_time: str | None = Field(default=None)
