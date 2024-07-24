# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.parts import BasePageInfo


class YoutubeListResponse(BaseModel):
    model_config = get_base_model_config()

    kind: str | None = Field(default=None)
    etag: str | None = Field(default=None)
    next_page_token: str | None = Field(default=None)
    prev_page_token: str | None = Field(default=None)
    page_info: BasePageInfo | None = Field(default=None)
    items: list | None = Field(default=[])
