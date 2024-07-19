# Python
from datetime import datetime
# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.part.base_status import BaseStatus


class VideoStatus(BaseStatus):
    model_config = get_base_model_config()

    upload_status: str | None = Field(default=None)
    failure_reason: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    publish_at: datetime | str | None = Field(default=None)
    license: str | None = Field(default=None)
    embeddable: bool | None = Field(default=None)
    public_stats_viewable: bool | None = Field(default=None)
    made_for_kids: bool | None = Field(default=None)
    self_declared_made_for_kids: bool | None = Field(default=None)
