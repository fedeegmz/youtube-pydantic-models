# Pydantic
from pydantic import BaseModel, Field
# models
from youtube_pydantic_models.models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.models.subpart.processing_progress import (
    ProcessingProgress
)


class BaseProcessingDetails(BaseModel):
    model_config = get_base_model_config()

    processing_status: str | None = Field(default=None)
    processing_progress: ProcessingProgress | None = Field(default=None)
    processing_failure_reason: str | None = Field(default=None)
    file_details_availability: str | None = Field(default=None)
    processing_issues_availability: str | None = Field(default=None)
    tag_suggestions_availability: str | None = Field(default=None)
    editor_suggestions_availability: str | None = Field(default=None)
    thumbnails_availability: str | None = Field(default=None)
