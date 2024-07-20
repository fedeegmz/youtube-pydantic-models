# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.subpart.channel import Channel
from models.subpart.image import Image
from models.subpart.watch import Watch


class BaseBrandingSettings(BaseModel):
    model_config = get_base_model_config()

    channel: Channel | None = Field(default=None)
    image: Image | None = Field(default=None)
    watch: Watch | None = Field(default=None)
