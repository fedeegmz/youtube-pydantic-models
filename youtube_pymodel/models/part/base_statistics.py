# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BaseStatistics(BaseModel):
    model_config = get_base_model_config()

    view_count: str | None = Field(default=None)
