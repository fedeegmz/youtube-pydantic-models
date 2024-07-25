from tests.youtube_client_for_testing import YoutubeClientForTesting


class TestSearchPlaylist(YoutubeClientForTesting):
    def test_search_playlist_with_available_channel_id(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        playlist = self.client.search(
            channel_id=channel_id,
            part="snippet",
            type="playlist"
        )
        data = playlist.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id'] is not None
        assert data['snippet'] is not None
        assert data['snippet']['channelId'] == channel_id
    
    def test_search_playlist_with_unavailable_channel_id(self):
        channel_id = ""
        playlist = self.client.search(
            channel_id=channel_id,
            part="snippet",
            type="playlist"
        )
        data = playlist.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id'] is not None
        assert data['snippet'] is not None
        assert data['snippet']['channelId'] != channel_id
    
    def test_search_playlist_with_available_channel_id_and_available_part(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        playlist = self.client.search(
            channel_id=channel_id,
            part="snippet",
            type="playlist"
        )
        data = playlist.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id'] is not None
        assert data['snippet'] is not None
        assert data['snippet']['channelId'] == channel_id
        assert len(data) == 4 # kind, etag, id, snippet
    
    def test_search_playlist_with_available_channel_id_and_unavailable_part(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        playlist = self.client.search(
            channel_id=channel_id,
            part="wrong",
            type="playlist"
        )

        assert playlist is None
