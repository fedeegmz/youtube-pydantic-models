# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.playlist_snippet import PlaylistSnippet


class VideoSnippet(PlaylistSnippet):
    model_config = get_base_model_config()

    tags: [str | None] = Field(default=[])
    category_id: str | None = Field(default=None)
    live_broadcast_content: str | None = Field(default=None)
    default_audio_language: str | None = Field(default=None)
