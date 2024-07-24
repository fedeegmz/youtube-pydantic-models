# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.part.page_info import (
    PageInfo
)


class YoutubeListResponse(BaseModel):
    model_config = get_base_model_config()

    kind: str | None = Field(default=None)
    etag: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None)
    prev_page_token: str | None = Field(default=None)
    page_info: PageInfo | None = Field(default=None)
    items: list[any | None] = Field(default=[])
