# Pydantic
from pydantic import BaseModel, Field
# models
from models.base_model_config import get_base_model_config


class BasePageInfo(BaseModel):
    model_config = get_base_model_config()
    
    total_results: int | None = Field(default=None)
    results_per_page: int | None = Field(default=None)
