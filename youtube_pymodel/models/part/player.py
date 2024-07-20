# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BasePlayer(BaseModel):
    model_config = get_base_model_config()

    embed_html: str | None = Field(default=None)


class VideoPlayer(BasePlayer):
    model_config = get_base_model_config()

    embed_height: int | None = Field(default=None)
    embed_width: int | None = Field(default=None)
