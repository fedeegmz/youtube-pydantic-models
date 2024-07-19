# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_statistics import BaseStatistics


class ChannelStatistics(BaseStatistics):
    model_config = get_base_model_config()

    subscriber_count: str | None = Field(default=None)
    hidden_subscriber_count: bool | None = Field(default=None)
    video_count: str | None = Field(default=None)
