# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BaseTopicDetails(BaseModel):
    model_config = get_base_model_config()

    topic_ids: list[str] | None = Field(default=None)
    topic_categories: list[str] | None = Field(default=None)


class VideoTopicDetails(BaseTopicDetails):
    model_config = get_base_model_config()

    relevant_topic_ids: list[str] | None = Field(default=None)
