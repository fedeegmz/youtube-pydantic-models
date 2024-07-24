import unittest
import json


class TestYoutubeResource(unittest.TestCase):
    def init_params(
        self,
        data_path: str,
        model
    ) -> tuple:
        data = self.get_json_data(data_path)
        if not data:
            raise Exception("example data not found")

        json_data = data["items"][0]
        model_data = model(
            **json_data
        ).model_dump(
            by_alias = True,
            exclude_none = True
        )

        return json_data, model_data

    def assert_equal_model_parts(self, part: str) -> None:
        json_part = self.json_data[part]
        model_part = self.model_data[part]
        print(json_part)
        print()
        print(model_part)
        if type(json_part) == dict and type(model_part) == dict:
            assert self.is_included_dict(json_part, model_part)
        else:
            assert json_part == model_part
    
    def get_json_data(self, file_name: str) -> dict | None:
        with open(
            f"tests/data/{file_name}",
            "r"
        ) as data:
            return json.loads(data.read())
        return None

    def is_included_dict(
        self,
        inner_dict: dict,
        outer_dict: dict
    ) -> bool:
        try:
            for key, value in inner_dict.items():
                if type(value) == dict:
                    self.is_included_dict(value, outer_dict[key])
                if value != outer_dict[key]:
                    return False
            return True
        except:
            return False
