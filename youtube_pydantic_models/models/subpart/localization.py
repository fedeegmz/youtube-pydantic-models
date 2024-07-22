# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class Localization(BaseModel):
    model_config = get_base_model_config()

    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
