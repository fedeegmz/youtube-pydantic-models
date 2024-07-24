from youtube_pydantic_models.search_resource import (
    YoutubeSearchResource
)
from tests.test_youtube_resource import TestYoutubeResource


class TestSearchChannelResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "search_channel_example_data.json",
            YoutubeSearchResource
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


class TestSearchPlaylistResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "search_playlist_example_data.json",
            YoutubeSearchResource
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


class TestSearchVideoResource(TestYoutubeResource):
    def setUp(self):
        params = self.init_params(
            "search_video_example_data.json",
            YoutubeSearchResource
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
