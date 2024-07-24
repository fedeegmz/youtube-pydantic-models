# Pydantic
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

def get_base_model_config() -> ConfigDict:
    return ConfigDict(
        arbitrary_types_allowed = True,
        alias_generator = to_camel
        # extra = "forbid"
    )
