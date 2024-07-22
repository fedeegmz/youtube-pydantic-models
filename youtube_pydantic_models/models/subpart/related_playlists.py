# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class RelatedPlaylists(BaseModel):
    model_config = get_base_model_config()

    likes: str | None = Field(default=None)
    uploads: str | None = Field(default=None)
    favorites: str | None = Field(default=None)
