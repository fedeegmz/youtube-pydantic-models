from tests.youtube_client_for_testing import YoutubeClientForTesting


class TestGetVideo(YoutubeClientForTesting):
    def test_get_available_video(self):
        video_id = "PJm8WNajZtw"
        video = self.client.get_video(
            id=video_id,
            part="snippet, contentDetails, statistics, topicDetails, status, player, recordingDetails, localizations, liveStreamingDetails"
        )
        data = video.model_dump(
            by_alias=True,
            exclude_none=True
        )
        
        assert data['id'] == video_id
        assert data['snippet'] is not None
        assert data['contentDetails'] is not None
        assert data['player'] is not None
        assert data['status'] is not None
    
    def test_get_unavailable_video(self):
        video_id = ""
        video = self.client.get_video(
            id=video_id,
            part="snippet, contentDetails, statistics, topicDetails, status, player, recordingDetails, localizations, liveStreamingDetails"
        )

        assert video is None
    
    def test_get_available_video_with_available_part(self):
        video_id = "PJm8WNajZtw"
        video = self.client.get_video(
            id=video_id,
            part="snippet, contentDetails, player, recordingDetails"
        )
        data = video.model_dump(
            by_alias=True,
            exclude_none=True
        )

        assert data['id'] == video_id
        assert data['snippet'] is not None
        assert data['contentDetails'] is not None
        assert data['player'] is not None
        assert data['recordingDetails'] is not None
        assert len(data) == 7 # kind, etag, id, snippet, contentDetails, player, recordingDetails
    
    def test_get_available_video_with_unvailable_part(self):
        video_id = "PJm8WNajZtw"
        video = self.client.get_video(
            id=video_id,
            part="wrong, player, localizations"
        )

        assert video is None
