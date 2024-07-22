# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class Watch(BaseModel):
    model_config = get_base_model_config()

    text_color: str | None = Field(default=None)
    background_color: str | None = Field(default=None)
    featured_playlist_id: str | None = Field(default=None)
