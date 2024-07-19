# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.part.thumbnail import ThumbnailPart


class BaseSnippet(BaseModel):
    model_config = get_base_model_config()

    published_at: datetime | str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    thumbnails: dict[str, ThumbnailPart] | None = Field(default=None)
