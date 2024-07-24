# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)


class YoutubeBaseResource(BaseModel):
    model_config = get_base_model_config()

    kind: str | None = Field(default=None)
    etag: str | None = Field(default=None)
