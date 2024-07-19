# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class AuditDetails(BaseModel):
    model_config = get_base_model_config()

    overall_good_standing: bool | None = Field(default=None)
    community_guide_lines_good_standing: bool | None = Field(default=None)
    copyright_strikes_good_standing: bool | None = Field(default=None)
    content_id_claims_good_standing: bool | None = Field(default=None)
