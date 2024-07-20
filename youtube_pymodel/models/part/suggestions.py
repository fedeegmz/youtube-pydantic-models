# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.subpart.tag_suggestion import TagSuggestions


class BaseSuggestions(BaseModel):
    model_config = get_base_model_config()

    processing_errors: list[str] | None = Field(default=None)
    processing_warnings: list[str] | None = Field(default=None)
    processing_hints: list[str] | None = Field(default=None)
    tag_suggestions: TagSuggestions | None = Field(default=None)
    editor_suggestions: list[str] | None = Field(default=None)
