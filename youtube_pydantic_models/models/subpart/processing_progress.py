# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class ProcessingProgress(BaseModel):
    model_config = get_base_model_config()

    parts_total: int | None = Field(default=None)
    parts_processed: int | None = Field(default=None)
    time_left_ms: int | None = Field(default=None)
