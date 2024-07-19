# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class RegionRestriction(BaseModel):
    model_config = get_base_model_config()

    allowed: [str | None] = Field(default=[])
    blocked: [str | None] = Field(default=[])
