from tests.youtube_client_for_testing import YoutubeClientForTesting


class TestGetChannel(YoutubeClientForTesting):
    def test_get_available_channel(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        channel = self.client.get_channel(
            id=channel_id,
            part="snippet, contentDetails, statistics, topicDetails, status, brandingSettings, contentOwnerDetails"
        )
        data = channel.model_dump(
            by_alias=True,
            exclude_none=True
        )

        assert data['id'] == channel_id
        assert data['snippet'] is not None
        assert data['contentDetails'] is not None
        assert data['statistics'] is not None
        assert data['topicDetails'] is not None
        assert data['status'] is not None
        assert data['brandingSettings'] is not None
        assert data['contentOwnerDetails'] is not None
    
    def test_get_unavailable_channel(self):
        channel_id = ""
        channel = self.client.get_channel(
            id=channel_id,
            part="snippet, contentDetails, statistics, topicDetails, status, brandingSettings, contentOwnerDetails"
        )

        assert channel is None
    
    def test_get_available_channel_with_available_part(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        channel = self.client.get_channel(
            id=channel_id,
            part="snippet, contentDetails"
        )
        data = channel.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id'] == channel_id
        assert data['snippet'] is not None
        assert data['contentDetails'] is not None
        assert len(data) == 5 # kind, etag, id, snippet, contentDetails
    
    def test_get_available_channel_with_unvailable_part(self):
        channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
        channel = self.client.get_channel(
            id=channel_id,
            part="wrongPart, snippet, contentDetails, statistics"
        )

        assert channel is None
