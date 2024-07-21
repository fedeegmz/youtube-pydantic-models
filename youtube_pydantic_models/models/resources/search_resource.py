# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.resources.base_resource import YoutubeBaseResource
from models.part.id import SearchId
from models.part.snippet import SearchSnippet


class YoutubeSearchResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: SearchId | None = Field(default=None)
    snippet: SearchSnippet | None = Field(default=None)
