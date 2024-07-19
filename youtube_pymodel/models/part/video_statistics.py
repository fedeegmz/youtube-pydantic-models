# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_statistics import BaseStatistics


class VideoStatistics(BaseStatistics):
    model_config = get_base_model_config()

    like_count: str | None = Field(default=None)
    dislike_count: str | None = Field(default=None)
    favorite_count: str | None = Field(default=None)
    comment_count: str | None = Field(default=None)
