# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class Thumbnail(BaseModel):
    model_config = get_base_model_config()
    
    url: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
