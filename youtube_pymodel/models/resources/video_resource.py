# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.resources.base_resource import YoutubeBaseResource
from models.part.id import Id
from models.part.video_snippet import VideoSnippet
from models.part.video_status import VideoStatus
from models.part.video_statistics import VideoStatistics
from models.part.video_content_details import VideoContentDetails
from models.part.video_player import VideoPlayer
from models.part.video_topic_details import VideoTopicDetails
from models.part.recording_details import RecordingDetails
from models.part.file_details import FileDetails
from models.part.processing_details import ProcessingDetails
from models.part.suggestions import Suggestions
from models.part.live_streaming_details import LiveStreamingDetails
from models.part.localization import Localization


class YoutubeVideoResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: VideoSnippet | None = Field(default=None)
    content_details: VideoContentDetails | None = Field(default=None)
    status: VideoStatus | None = Field(default=None)
    statistics: VideoStatistics | None = Field(default=None)
    player: VideoPlayer | None = Field(default=None)
    topic_details: VideoTopicDetails | None = Field(default=None)
    recording_details: RecordingDetails | None = Field(default=None)
    file_details : FileDetails | None = Field(default=None)
    processing_details: ProcessingDetails | None = Field(default=None)
    suggestions: Suggestions | None = Field(default=None)
    live_streaming_details: LiveStreamingDetails | None = Field(default=None)
    localizations: {str, Localization} | None = Field(default=None)
