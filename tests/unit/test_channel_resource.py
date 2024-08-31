from youtube_pydantic_models.channel_resource import (
    YoutubeChannelResource
)
from tests.test_youtube_resource import TestYoutubeResource


class TestChannelResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "channel_example_data.json",
            YoutubeChannelResource
        )
        self.json_data = params[0]
        self.model_data = params[1]
    
    def test_equal_kind_part(self):
        self.assert_equal_model_parts("kind")
    
    def test_equal_etag_part(self):
        self.assert_equal_model_parts("etag")
    
    def test_equal_id_part(self):
        self.assert_equal_model_parts("id")

    def test_equal_snippet_part(self):
        self.assert_equal_model_parts("snippet")
    
    def test_equal_content_details_part(self):
        self.assert_equal_model_parts("contentDetails")
    
    def test_equal_statistics_part(self):
        self.assert_equal_model_parts("statistics")
    
    def test_equal_topic_details_part(self):
        self.assert_equal_model_parts("topicDetails")
    
    def test_equal_status_part(self):
        self.assert_equal_model_parts("status")
    
    def test_equal_branding_settings_part(self):
        self.assert_equal_model_parts("brandingSettings")
