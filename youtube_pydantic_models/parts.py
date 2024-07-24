from datetime import datetime
from pydantic import BaseModel, Field
from youtube_pydantic_models.base_model_config import (
    get_base_model_config
)
from youtube_pydantic_models._subparts.channel import (
    Channel
)
from youtube_pydantic_models._subparts.image import (
    Image
)
from youtube_pydantic_models._subparts.watch import (
    Watch
)
from youtube_pydantic_models._subparts.related_playlists import (
    RelatedPlaylists
)
from youtube_pydantic_models._subparts.region_restriction import (
    RegionRestriction
)
from youtube_pydantic_models._subparts.content_rating import (
    ContentRating
)
from youtube_pydantic_models._subparts.audio_video_stream import (
    AudioStream,
    VideoStream
)
from youtube_pydantic_models._subparts.processing_progress import (
    ProcessingProgress
)
from youtube_pydantic_models._subparts.thumbnail import (
    Thumbnail
)
from youtube_pydantic_models._subparts.localized import (
    Localized
)
from youtube_pydantic_models._subparts.tag_suggestion import (
    TagSuggestions
)


class BaseAuditDetails(BaseModel):
    model_config = get_base_model_config()

    overall_good_standing: bool | None = Field(default=None)
    community_guide_lines_good_standing: bool | None = Field(default=None)
    copyright_strikes_good_standing: bool | None = Field(default=None)
    content_id_claims_good_standing: bool | None = Field(default=None)


class BaseBrandingSettings(BaseModel):
    model_config = get_base_model_config()

    channel: Channel | None = Field(default=None)
    image: Image | None = Field(default=None)
    watch: Watch | None = Field(default=None)


class ChannelContentDetails(BaseModel):
    model_config = get_base_model_config()

    related_playlists: RelatedPlaylists | None = Field(default=None)


class PlaylistContentDetails(BaseModel):
    model_config = get_base_model_config()

    item_count: int | None = Field(default=None)


class VideoContentDetails(BaseModel):
    model_config = get_base_model_config()

    duration: str | None = Field(default=None)
    dimension: str | None = Field(default=None)
    definition: str | None = Field(default=None)
    caption: str | None = Field(default=None)
    licensed_content: bool | None = Field(default=None)
    region_restriction: RegionRestriction | None = Field(default=None)
    content_rating: ContentRating | None = Field(default=None)
    projection: str | None = Field(default=None)
    has_custom_thumbnail: bool | None = Field(default=None)


class BaseContentOwnerDetails(BaseModel):
    model_config = get_base_model_config()

    content_owner: str | None = Field(default=None)
    time_linked: datetime | str | None = Field(default=None)


class BaseFileDetails(BaseModel):
    model_config = get_base_model_config()

    file_name: str | None = Field(default=None)
    file_size: int | None = Field(default=None)
    file_type: str | None = Field(default=None)
    container: str | None = Field(default=None)
    video_streams: list[VideoStream] | None = Field(default=None)
    audio_streams: list[AudioStream] | None = Field(default=None)
    duration_ms: int | None = Field(default=None)
    bitrate_bps: int | None = Field(default=None)
    creation_time: str | None = Field(default=None)


class SearchId(BaseModel):
    model_config = get_base_model_config()

    kind: str | None = Field(default=None)
    video_id: str | None = Field(default=None)
    channel_id: str | None = Field(default=None)
    playlist_id: str | None = Field(default=None)


class BaseLiveStreamingDetails(BaseModel):
    model_config = get_base_model_config()

    actual_start_time: datetime | str | None = Field(default=None)
    actual_end_time: datetime | str | None = Field(default=None)
    scheduled_start_time: datetime | str | None = Field(default=None)
    scheduled_end_time: datetime | str | None = Field(default=None)
    concurrent_viewers: int | None = Field(default=None)
    active_live_chat_id: str | None = Field(default=None)


class BasePageInfo(BaseModel):
    model_config = get_base_model_config()
    
    total_results: int | None = Field(default=None)
    results_per_page: int | None = Field(default=None)


class BasePlayer(BaseModel):
    model_config = get_base_model_config()

    embed_html: str | None = Field(default=None)


class VideoPlayer(BasePlayer):
    model_config = get_base_model_config()

    embed_height: int | None = Field(default=None)
    embed_width: int | None = Field(default=None)


class BaseProcessingDetails(BaseModel):
    model_config = get_base_model_config()

    processing_status: str | None = Field(default=None)
    processing_progress: ProcessingProgress | None = Field(default=None)
    processing_failure_reason: str | None = Field(default=None)
    file_details_availability: str | None = Field(default=None)
    processing_issues_availability: str | None = Field(default=None)
    tag_suggestions_availability: str | None = Field(default=None)
    editor_suggestions_availability: str | None = Field(default=None)
    thumbnails_availability: str | None = Field(default=None)


class BaseRecordingDetails(BaseModel):
    model_config = get_base_model_config()

    recording_date: datetime | str | None = Field(default=None)


class BaseSnippet(BaseModel):
    model_config = get_base_model_config()

    published_at: datetime | str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    thumbnails: dict[str, Thumbnail] | None = Field(default=None)


class SearchSnippet(BaseSnippet):
    model_config = get_base_model_config()

    channel_id: str | None = Field(default=None)
    channel_title: str | None = Field(default=None)
    live_broadcast_content: str | None = Field(default=None)
    publish_time: datetime | str | None = Field(default=None)


class ChannelSnippet(BaseSnippet):
    model_config = get_base_model_config()

    custom_url: str | None = Field(default=None)
    default_language: str | None = Field(default=None)
    localized: Localized | None = Field(default=None)
    country: str | None = Field(default=None)


class PlaylistSnippet(BaseSnippet):
    model_config = get_base_model_config()
    
    channel_id: str | None = Field(default=None)
    channel_title: str | None = Field(default=None)
    default_language: str | None = Field(default=None)
    localized: Localized | None = Field(default=None)


class VideoSnippet(PlaylistSnippet):
    model_config = get_base_model_config()

    tags: list[str] | None = Field(default=None)
    category_id: str | None = Field(default=None)
    live_broadcast_content: str | None = Field(default=None)
    default_audio_language: str | None = Field(default=None)


class BaseStatistics(BaseModel):
    model_config = get_base_model_config()

    view_count: str | None = Field(default=None)


class ChannelStatistics(BaseStatistics):
    model_config = get_base_model_config()

    subscriber_count: str | None = Field(default=None)
    hidden_subscriber_count: bool | None = Field(default=None)
    video_count: str | None = Field(default=None)


class VideoStatistics(BaseStatistics):
    model_config = get_base_model_config()

    like_count: str | None = Field(default=None)
    dislike_count: str | None = Field(default=None)
    favorite_count: str | None = Field(default=None)
    comment_count: str | None = Field(default=None)


class BaseStatus(BaseModel):
    model_config = get_base_model_config()

    privacy_status: str | None = Field(default=None)


class SharedStatus(BaseStatus):
    model_config = get_base_model_config()

    made_for_kids: bool | None = Field(default=None)
    self_declared_made_for_kids: bool | None = Field(default=None)


class ChannelStatus(SharedStatus):
    model_config = get_base_model_config()

    is_linked: bool | None = Field(default=None)
    long_uploads_status: str | None = Field(default=None)


class VideoStatus(SharedStatus):
    model_config = get_base_model_config()

    upload_status: str | None = Field(default=None)
    failure_reason: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    publish_at: datetime | str | None = Field(default=None)
    license: str | None = Field(default=None)
    embeddable: bool | None = Field(default=None)
    public_stats_viewable: bool | None = Field(default=None)


class BaseSuggestions(BaseModel):
    model_config = get_base_model_config()

    processing_errors: list[str] | None = Field(default=None)
    processing_warnings: list[str] | None = Field(default=None)
    processing_hints: list[str] | None = Field(default=None)
    tag_suggestions: TagSuggestions | None = Field(default=None)
    editor_suggestions: list[str] | None = Field(default=None)


class BaseTopicDetails(BaseModel):
    model_config = get_base_model_config()

    topic_ids: list[str] | None = Field(default=None)
    topic_categories: list[str] | None = Field(default=None)


class VideoTopicDetails(BaseTopicDetails):
    model_config = get_base_model_config()

    relevant_topic_ids: list[str] | None = Field(default=None)
