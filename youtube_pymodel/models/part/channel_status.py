# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_status import BaseStatus


class ChannelStatus(BaseStatus):
    model_config = get_base_model_config()

    is_linked: bool | None = Field(default=None)
    long_uploads_status: str | None = Field(default=None)
    made_for_kids: bool | None = Field(default=None)
    self_declared_made_for_kids: bool | None = Field(default=None)
