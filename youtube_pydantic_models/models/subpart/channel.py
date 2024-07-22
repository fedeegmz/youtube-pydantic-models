# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)


class Channel(BaseModel):
    model_config = get_base_model_config()

    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    keywords: str | None = Field(default=None)
    tracking_analytics_account_id: str | None = Field(default=None)
    unsubscribed_trailer: str | None = Field(default=None)
    country: str | None = Field(default=None)
    default_language: str | None = Field(default=None)
