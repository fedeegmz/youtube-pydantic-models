# Pydantic
from pydantic import Field
# models
from models.base_model_config import get_base_model_config
from models.resources.base_resource import YoutubeBaseResource
from models.part.channel_snippet import ChannelSnippet
from models.part.channel_content_details import ChannelContentDetails
from models.part.channel_statistics import ChannelStatistics
from models.part.base_topic_details import BaseTopicDetails
from models.part.channel_status import ChannelStatus
from models.part.branding_settings import BrandingSettings
from models.part.audit_details import AuditDetails
from models.part.content_owner_details import ContentOwnerDetails
from models.part.localization import Localization


class YoutubeChannelResource(YoutubeBaseResource):
    model_config = get_base_model_config()

    id: str | None = Field(default=None)
    snippet: ChannelSnippet | None = Field(default=None)
    content_details: ChannelContentDetails | None = Field(default=None)
    statistics: ChannelStatistics | None = Field(default=None)
    topic_details: BaseTopicDetails | None = Field(default=None)
    status: ChannelStatus | None = Field(default=None)
    branding_settings: BrandingSettings | None = Field(default=None)
    audit_details: AuditDetails | None = Field(default=None)
    content_owner_details: ContentOwnerDetails | None = Field(default=None)
    localizations: {str, Localization} | None = Field(default=None)
