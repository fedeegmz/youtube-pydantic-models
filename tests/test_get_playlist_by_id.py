from tests.youtube_client_for_testing import YoutubeClientForTesting


class TestGetPlaylist(YoutubeClientForTesting):
    def test_get_available_playlist(self):
        playlist_id = "PLOU2XLYxmsIL-LSajwT6_VviFWrDChEJX"
        playlist = self.client.get_playlist(
            id=playlist_id,
            part="snippet, contentDetails, player, status, localizations"
        )
        data = playlist.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id'] == playlist_id
        assert data['snippet'] is not None
        assert data['contentDetails'] is not None
        assert data['player'] is not None
        assert data['status'] is not None
    
    def test_get_unavailable_playlist(self):
        playlist_id = ""
        playlist = self.client.get_playlist(
            id=playlist_id,
            part="snippet, contentDetails, player, status, localizations"
        )

        assert playlist is None
    
    def test_get_available_playlist_with_available_part(self):
        playlist_id = "PLOU2XLYxmsIL-LSajwT6_VviFWrDChEJX"
        playlist = self.client.get_playlist(
            id=playlist_id,
            part="snippet, contentDetails, player"
        )
        data = playlist.model_dump(
            by_alias=True,
            exclude_none=True
        )

        assert data['id'] == playlist_id
        assert data['snippet'] is not None
        assert data['contentDetails'] is not None
        assert data['player'] is not None
        assert len(data) == 6 # kind, etag, id, snippet, contentDetails, player
    
    def test_get_available_playlist_with_unvailable_part(self):
        playlist_id = "PLOU2XLYxmsIL-LSajwT6_VviFWrDChEJX"
        playlist = self.client.get_playlist(
            id=playlist_id,
            part="wrong, player, localizations"
        )

        assert playlist is None
