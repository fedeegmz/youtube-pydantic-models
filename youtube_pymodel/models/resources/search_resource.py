# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.resources.base_resource import YoutubeBaseResource
from models.part.id import Id
from models.part.search_snippet import SearchSnippet


class YoutubeSearchResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: Id | None = Field(default=None)
    snippet: SearchSnippet | None = Field(default=None)
