# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.resources.base_resource import YoutubeBaseResource
from models.part.snippet import PlaylistSnippet
from models.part.status import BaseStatus
from models.part.content_details import PlaylistContentDetails
from models.part.player import BasePlayer
from models.subpart.localization import Localization


class YoutubePlaylistResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: PlaylistSnippet | None = Field(default=None)
    status: BaseStatus | None = Field(default=None)
    content_details: PlaylistContentDetails | None = Field(default=None)
    player: BasePlayer | None = Field(default=None)
    localizations: dict[str, Localization] | None = Field(default=None)
