# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config
from models.part.region_restriction import RegionRestriction
from models.part.content_rating import ContentRating


class VideoContentDetails(BaseModel):
    model_config = get_base_model_config()

    duration: str | None = Field(default=None)
    dimension: str | None = Field(default=None)
    definition: str | None = Field(default=None)
    caption: str | None = Field(default=None)
    licensed_content: bool | None = Field(default=None)
    region_restriction: RegionRestriction | None = Field(default=None)
    content_rating: ContentRating | None = Field(default=None)
    projection: str | None = Field(default=None)
    has_custom_thumbnail: bool | None = Field(default=None)
