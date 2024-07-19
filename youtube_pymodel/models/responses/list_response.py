# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.part.page_info import PageInfoPart


class YoutubeListResponse(BaseModel):
    model_config = get_base_model_config()

    kind: str | None = Field(default=None)
    etag: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None)
    prev_page_token: str | None = Field(default=None)
    page_info: PageInfoPart | None = Field(default=None)
    items: list[any | None] = Field(default=[])
