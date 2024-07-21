# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class Image(BaseModel):
    model_config = get_base_model_config()

    banner_external_url: str | None = Field(default=None)
