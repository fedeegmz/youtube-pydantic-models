# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_snippet import BaseSnippet
from models.part.localized import LocalizedPart


class ChannelSnippet(BaseSnippet):
    model_config = get_base_model_config()

    custom_url: str | None = Field(default=None)
    default_language: str | None = Field(default=None)
    localized: LocalizedPart | None = Field(default=None)
    country: str | None = Field(default=None)
