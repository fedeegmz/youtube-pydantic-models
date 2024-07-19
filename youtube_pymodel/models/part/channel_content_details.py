# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.part.related_playlists import RelatedPlaylists


class ChannelContentDetails(BaseModel):
    model_config = get_base_model_config()

    related_playlists: RelatedPlaylists | None = Field(default=None)
