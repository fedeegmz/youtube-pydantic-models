# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class TagSuggestions(BaseModel):
    model_config = get_base_model_config()

    tag: str | None = Field(default=None)
    category_restricts: list[str] | None = Field(default=None)
