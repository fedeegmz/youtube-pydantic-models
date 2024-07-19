# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_topic_details import BaseTopicDetails


class BaseTopicDetails(BaseTopicDetails):
    model_config = get_base_model_config()

    relevant_topic_ids: list[str | None] = Field(default=[])
