# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.resources.base_resource import YoutubeBaseResource
from models.part.id import Id
from models.part.playlist_snippet import PlaylistSnippet
from models.part.base_status import BaseStatus
from models.part.playlist_content_details import PlaylistContentDetails
from models.part.base_player import BasePlayer
from models.part.localization import Localization


class YoutubePlaylistResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: PlaylistSnippet | None = Field(default=None)
    status: BaseStatus | None = Field(default=None)
    content_details: PlaylistContentDetails | None = Field(default=None)
    player: BasePlayer | None = Field(default=None)
    localizations: {str, Localization} | None = Field(default=None)
