# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class SearchId(BaseModel):
    model_config = get_base_model_config()

    kind: str | None = Field(default=None)
    video_id: str | None = Field(default=None)
    channel_id: str | None = Field(default=None)
    playlist_id: str | None = Field(default=None)
