# Pydantic
from pydantic import Field
# models
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.base_resource import (
    YoutubeBaseResource
)
from youtube_pydantic_models.parts import PlaylistSnippet
from youtube_pydantic_models.parts import BaseStatus
from youtube_pydantic_models.parts import PlaylistContentDetails
from youtube_pydantic_models.parts import BasePlayer
from youtube_pydantic_models._subparts.localization import (
    Localization
)


class YoutubePlaylistResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: PlaylistSnippet | None = Field(default=None)
    status: BaseStatus | None = Field(default=None)
    content_details: PlaylistContentDetails | None = Field(default=None)
    player: BasePlayer | None = Field(default=None)
    localizations: dict[str, Localization] | None = Field(default=None)
