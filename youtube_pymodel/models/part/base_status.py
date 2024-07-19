# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BaseStatus(BaseModel):
    model_config = get_base_model_config()

    privacy_status: str | None = Field(default=None)
