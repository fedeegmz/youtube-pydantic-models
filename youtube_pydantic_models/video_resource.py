# Pydantic
from pydantic import Field
# models
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models.base_resource import (
    YoutubeBaseResource
)
from youtube_pydantic_models._parts.snippet import (
    VideoSnippet
)
from youtube_pydantic_models._parts.content_details import (
    VideoContentDetails
)
from youtube_pydantic_models._parts.status import (
    VideoStatus
)
from youtube_pydantic_models._parts.statistics import (
    VideoStatistics
)
from youtube_pydantic_models._parts.player import (
    VideoPlayer
)
from youtube_pydantic_models._parts.topic_details import (
    VideoTopicDetails
)
from youtube_pydantic_models._parts.recording_details import (
    BaseRecordingDetails
)
from youtube_pydantic_models._parts.file_details import (
    BaseFileDetails
)
from youtube_pydantic_models._parts.processing_details import (
    BaseProcessingDetails
)
from youtube_pydantic_models._parts.suggestions import (
    BaseSuggestions
)
from youtube_pydantic_models._parts.live_streaming_details import (
    BaseLiveStreamingDetails
)
from youtube_pydantic_models._subparts.localization import (
    Localization
)


class YoutubeVideoResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: VideoSnippet | None = Field(default=None)
    content_details: VideoContentDetails | None = Field(default=None)
    status: VideoStatus | None = Field(default=None)
    statistics: VideoStatistics | None = Field(default=None)
    player: VideoPlayer | None = Field(default=None)
    topic_details: VideoTopicDetails | None = Field(default=None)
    recording_details: BaseRecordingDetails | None = Field(default=None)
    file_details : BaseFileDetails | None = Field(default=None)
    processing_details: BaseProcessingDetails | None = Field(default=None)
    suggestions: BaseSuggestions | None = Field(default=None)
    live_streaming_details: BaseLiveStreamingDetails | None = Field(default=None)
    localizations: dict[str, Localization] | None = Field(default=None)
