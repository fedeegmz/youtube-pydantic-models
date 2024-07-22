# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.models.subpart.channel import (
    Channel
)
from youtube_pydantic_models.models.subpart.image import (
    Image
)
from youtube_pydantic_models.models.subpart.watch import (
    Watch
)


class BaseBrandingSettings(BaseModel):
    model_config = get_base_model_config()

    channel: Channel | None = Field(default=None)
    image: Image | None = Field(default=None)
    watch: Watch | None = Field(default=None)
