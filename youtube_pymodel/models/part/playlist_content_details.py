# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class PlaylistContentDetails(BaseModel):
    model_config = get_base_model_config()

    item_count: int | None = Field(default=None)
