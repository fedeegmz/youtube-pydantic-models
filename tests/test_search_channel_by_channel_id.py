from tests.youtube_client_for_testing import YoutubeClientForTesting


class TestSearchChannel(YoutubeClientForTesting):
    def test_search_available_channel(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        channel = self.client.search(
            channel_id=channel_id,
            part="id, snippet",
            type="channel"
        )
        data = channel.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id']['channelId'] == channel_id
        assert data['snippet'] is not None
    
    def test_search_unavailable_channel(self):
        channel_id = ""
        channel = self.client.search(
            channel_id=channel_id,
            part="id, snippet",
            type="channel"
        )
        data = channel.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id']['channelId'] != channel_id
        assert data['snippet'] is not None
    
    def test_search_available_channel_with_available_part(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        channel = self.client.search(
            channel_id=channel_id,
            part="snippet",
            type="channel"
        )
        data = channel.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id']['channelId'] == channel_id
        assert data['snippet'] is not None
        assert len(data) == 4 # kind, etag, id, snippet
    
    def test_search_available_channel_with_unvailable_part(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        channel = self.client.search(
            channel_id=channel_id,
            part="wrongPart, snippet",
            type="channel"
        )

        assert channel is None
