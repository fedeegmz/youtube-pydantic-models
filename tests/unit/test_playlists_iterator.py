from unittest import TestCase, mock
from youtube_pydantic_models.main import YoutubeClient
from youtube_pydantic_models.playlist_resource import YoutubePlaylistResource
from tests.data.mock.list_of_playlists import playlists_for_mocking


class TestPlaylistsIterator(TestCase):
    @mock.patch.object(YoutubeClient, "_get_request")
    def test_iter_playlists_method_from_youtube_client_should_yield_a_playlist_resource(
        self, mock_method
    ):
        mock_method.return_value = {"items": playlists_for_mocking}
        client = YoutubeClient("example-api-key")

        for playlist in client.iter_playlists("example-channel-id"):
            assert playlist
            assert isinstance(playlist, YoutubePlaylistResource)
