# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.subpart.thumbnail import Thumbnail
from models.subpart.localized import Localized


class BaseSnippet(BaseModel):
    model_config = get_base_model_config()

    published_at: datetime | str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    thumbnails: dict[str, Thumbnail] | None = Field(default=None)


class SearchSnippet(BaseSnippet):
    model_config = get_base_model_config()

    channel_id: str | None = Field(default=None)
    channel_title: str | None = Field(default=None)
    live_broadcast_content: str | None = Field(default=None)
    publish_time: datetime | str | None = Field(default=None)


class ChannelSnippet(BaseSnippet):
    model_config = get_base_model_config()

    custom_url: str | None = Field(default=None)
    default_language: str | None = Field(default=None)
    localized: Localized | None = Field(default=None)
    country: str | None = Field(default=None)


class PlaylistSnippet(BaseSnippet):
    model_config = get_base_model_config()
    
    channel_id: str | None = Field(default=None)
    channel_title: str | None = Field(default=None)
    default_language: str | None = Field(default=None)
    localized: Localized | None = Field(default=None)


class VideoSnippet(PlaylistSnippet):
    model_config = get_base_model_config()

    tags: list[str] | None = Field(default=None)
    category_id: str | None = Field(default=None)
    live_broadcast_content: str | None = Field(default=None)
    default_audio_language: str | None = Field(default=None)
