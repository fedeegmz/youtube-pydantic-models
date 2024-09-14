from unittest import TestCase, mock
from youtube_pydantic_models.main import YoutubeClient
from youtube_pydantic_models.video_resource import YoutubeVideoResource
from tests.data.mock.list_of_search_videos import search_videos_for_mocking
from tests.data.mock.video import video_for_mocking


class TestVideoIterator(TestCase):
    @mock.patch.object(YoutubeClient, "_get_request")
    @mock.patch.object(YoutubeClient, "get_video")
    def test_iter_videos_method_from_youtube_client_should_yield_a_video_resource(
        self, mock_get_video, mock_get_request
    ):
        mock_get_request.return_value = search_videos_for_mocking
        mock_get_video.return_value = YoutubeVideoResource(**video_for_mocking)
        client = YoutubeClient("example-api-key")

        for video in client.iter_videos("example-channel-id"):
            assert video
            assert isinstance(video, YoutubeVideoResource)
        mock_get_request.assert_called()
        mock_get_video.assert_called()
