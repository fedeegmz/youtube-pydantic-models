# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_snippet import BaseSnippet


class SearchSnippet(BaseSnippet):
    model_config = get_base_model_config()

    channel_id: str | None = Field(default=None)
    channel_title: str | None = Field(default=None)
    live_broadcast_content: str | None = Field(default=None)
