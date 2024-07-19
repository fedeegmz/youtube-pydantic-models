# Pydantic
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

def get_base_model_config() -> ConfigDict:
    return ConfigDict(
        alias_generators = to_camel
    )
