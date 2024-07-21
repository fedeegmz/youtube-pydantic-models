# Python
from datetime import datetime
# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BaseContentOwnerDetails(BaseModel):
    model_config = get_base_model_config()

    content_owner: str | None = Field(default=None)
    time_linked: datetime | str | None = Field(default=None)
