# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_player import BasePlayer


class VideoPlayer(BasePlayer):
    model_config = get_base_model_config()

    embed_height: int | None = Field(default=None)
    embed_width: int | None = Field(default=None)
