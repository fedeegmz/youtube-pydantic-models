# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.models.subpart.audio_video_stream import (
    AudioStream,
    VideoStream
)


class BaseFileDetails(BaseModel):
    model_config = get_base_model_config()

    file_name: str | None = Field(default=None)
    file_size: int | None = Field(default=None)
    file_type: str | None = Field(default=None)
    container: str | None = Field(default=None)
    video_streams: list[VideoStream] | None = Field(default=None)
    audio_streams: list[AudioStream] | None = Field(default=None)
    duration_ms: int | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    creation_time: str | None = Field(default=None)
