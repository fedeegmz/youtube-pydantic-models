# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.part.channel import Channel
from models.part.watch import Watch


class BrandingSettings(BaseModel):
    model_config = get_base_model_config()

    channel: Channel | None = Field(default=None)
    watch: Watch | None = Field(default=None)
